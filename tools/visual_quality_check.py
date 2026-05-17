"""
Quality-control gate for portfolio SVG visuals.

The checks are intentionally conservative and deterministic:
- SVG parses as XML
- root viewBox is present and large enough for GitHub presentation
- title and description metadata are present
- text elements use readable font sizes and stay inside the viewBox
- card-tagged groups keep text inside their card bounds
- arrow-tagged paths use a defined marker-end
- polished artifacts include a frame, footer, rounded cards, and version metadata

Usage:
    python tools/visual_quality_check.py projects --report project-management/visual-quality-report.md
"""

from __future__ import annotations

import argparse
import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path


MIN_WIDTH = 1000
MIN_HEIGHT = 600
MIN_FONT_SIZE = 11
MAX_TEXT_CHARS = 92
CARD_PADDING = 18
MIN_CARD_RADIUS = 18
MIN_FRAME_RADIUS = 24


@dataclass
class CheckResult:
    path: Path
    status: str = "PASS"
    notes: list[str] = field(default_factory=list)

    def fail(self, message: str) -> None:
        self.status = "FAIL"
        self.notes.append(message)

    def warn(self, message: str) -> None:
        self.notes.append(f"WARN: {message}")


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def attr_float(node: ET.Element, name: str, default: float = 0.0) -> float:
    raw = node.attrib.get(name, str(default))
    match = re.search(r"-?\d+(?:\.\d+)?", raw)
    return float(match.group(0)) if match else default


def text_value(node: ET.Element) -> str:
    return " ".join(part.strip() for part in node.itertext() if part.strip())


def element_font_size(node: ET.Element) -> float:
    if "font-size" in node.attrib:
        return attr_float(node, "font-size", MIN_FONT_SIZE)
    style = node.attrib.get("style", "")
    match = re.search(r"font-size\s*:\s*(\d+(?:\.\d+)?)", style)
    return float(match.group(1)) if match else MIN_FONT_SIZE


def parse_viewbox(root: ET.Element) -> tuple[float, float, float, float] | None:
    raw = root.attrib.get("viewBox")
    if not raw:
        return None
    values = [float(part) for part in re.split(r"[ ,]+", raw.strip()) if part]
    if len(values) != 4:
        return None
    return values[0], values[1], values[2], values[3]


def collect_ids(root: ET.Element) -> set[str]:
    return {node.attrib["id"] for node in root.iter() if "id" in node.attrib}


def estimate_text_width(value: str, font_size: float) -> float:
    return len(value) * font_size * 0.55


def check_card_group(result: CheckResult, group: ET.Element) -> None:
    rect = next((node for node in group.iter() if local_name(node.tag) == "rect"), None)
    if rect is None:
        result.fail("card group is missing a rect")
        return
    x = attr_float(rect, "x")
    y = attr_float(rect, "y")
    width = attr_float(rect, "width")
    height = attr_float(rect, "height")
    radius = attr_float(rect, "rx")
    if radius < MIN_CARD_RADIUS:
        result.fail(f"card radius below polish threshold: {radius:g}")
    if "cardShadow" not in rect.attrib.get("filter", ""):
        result.fail("card is missing the standard shadow treatment")
    right = x + width - CARD_PADDING
    bottom = y + height - CARD_PADDING
    for text in [node for node in group.iter() if local_name(node.tag) == "text"]:
        content = text_value(text)
        if not content:
            continue
        font_size = element_font_size(text)
        tx = attr_float(text, "x")
        ty = attr_float(text, "y")
        estimated_right = tx + estimate_text_width(content, font_size)
        if tx < x + CARD_PADDING - 2:
            result.fail(f"text starts outside card padding: {content[:48]}")
        if estimated_right > right + 4:
            result.fail(f"text may overflow card width: {content[:68]}")
        if ty < y + CARD_PADDING or ty > bottom + 4:
            result.fail(f"text may overflow card height: {content[:68]}")


def check_svg(path: Path) -> CheckResult:
    result = CheckResult(path=path)
    try:
        tree = ET.parse(path)
    except ET.ParseError as exc:
        result.fail(f"XML parse error: {exc}")
        return result

    root = tree.getroot()
    if root.attrib.get("data-qc-polish") != "true":
        result.fail("missing data-qc-polish marker")
    version_raw = root.attrib.get("data-qc-version", "0")
    try:
        version = int(version_raw)
    except ValueError:
        version = 0
    if version < 2:
        result.fail(f"visual QC version is too old: {version_raw}")

    viewbox = parse_viewbox(root)
    if viewbox is None:
        result.fail("missing or invalid viewBox")
        width = height = 0
    else:
        _, _, width, height = viewbox
        if width < MIN_WIDTH or height < MIN_HEIGHT:
            result.fail(f"viewBox too small: {width:g}x{height:g}")

    titles = [node for node in root.iter() if local_name(node.tag) == "title" and text_value(node)]
    descs = [node for node in root.iter() if local_name(node.tag) == "desc" and text_value(node)]
    if not titles:
        result.fail("missing title metadata")
    if not descs:
        result.fail("missing desc metadata")

    frames = [node for node in root.iter() if node.attrib.get("data-qc-frame") == "true"]
    if not frames:
        result.fail("missing polished frame marker")
    else:
        frame_radius = attr_float(frames[0], "rx")
        if frame_radius < MIN_FRAME_RADIUS:
            result.fail(f"frame radius below polish threshold: {frame_radius:g}")

    footers = [node for node in root.iter() if node.attrib.get("data-qc-footer") == "true"]
    if not footers:
        result.fail("missing source/QC footer")

    if "QC-ready artifact" not in text_value(root):
        result.fail("missing QC-ready header marker")

    for text in [node for node in root.iter() if local_name(node.tag) == "text"]:
        content = text_value(text)
        if not content:
            continue
        font_size = element_font_size(text)
        if font_size < MIN_FONT_SIZE:
            result.fail(f"font size below readable threshold: {content[:48]}")
        if len(content) > MAX_TEXT_CHARS:
            result.fail(f"text line is too long for reliable rendering: {content[:68]}")
        x = attr_float(text, "x")
        y = attr_float(text, "y")
        if viewbox is not None and (x < 0 or y < 0 or x > width or y > height):
            result.fail(f"text coordinate outside viewBox: {content[:48]}")

    card_groups = [node for node in root.iter() if node.attrib.get("data-qc-card") == "true"]
    if not card_groups:
        result.warn("no data-qc-card groups found")
    for group in card_groups:
        check_card_group(result, group)

    ids = collect_ids(root)
    arrows = [node for node in root.iter() if node.attrib.get("data-qc-arrow") == "true"]
    for arrow in arrows:
        marker = arrow.attrib.get("marker-end", "")
        match = re.search(r"url\(#([^)]+)\)", marker)
        if not match:
            result.fail("arrow path missing marker-end")
        elif match.group(1) not in ids:
            result.fail(f"arrow marker is not defined: {match.group(1)}")

    return result


def discover_svg(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if path.is_file() and path.suffix.lower() == ".svg":
            files.append(path)
        elif path.is_dir():
            files.extend(sorted(path.rglob("*.svg")))
    return sorted(set(files))


def build_report(results: list[CheckResult]) -> str:
    passed = sum(1 for result in results if result.status == "PASS")
    failed = len(results) - passed
    lines = [
        "# Visual Quality Report",
        "",
        "Generated by `tools/visual_quality_check.py`.",
        "",
        "## Summary",
        "",
        f"- SVG files checked: {len(results)}",
        f"- Passed: {passed}",
        f"- Failed: {failed}",
        "",
        "## Checks",
        "",
        "| File | Status | Notes |",
        "|---|---|---|",
    ]
    for result in results:
        notes = "<br>".join(result.notes) if result.notes else "All checks passed"
        lines.append(f"| `{result.path.as_posix()}` | {result.status} | {notes} |")
    lines.extend(
        [
            "",
            "## Gate Criteria",
            "",
            "- SVG must parse as XML.",
            "- SVG must include a `viewBox` of at least 1000 by 600.",
            "- SVG must include `title` and `desc` metadata.",
            "- Text must use readable font sizes and remain within the viewBox.",
            "- Card-tagged groups must keep estimated text width and height inside the card.",
            "- Arrow-tagged paths must use a defined marker-end.",
            "- Polished visuals must include version metadata, a rounded frame, a source/QC footer, and the QC-ready marker.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run SVG visual quality checks.")
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()

    files = discover_svg(args.paths)
    results = [check_svg(path) for path in files]
    report = build_report(results)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(report, encoding="utf-8")
    print(report)
    return 1 if any(result.status == "FAIL" for result in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())

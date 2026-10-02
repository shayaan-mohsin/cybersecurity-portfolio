"""Check local links, image alt text and SVG metadata; not external URLs or rendering."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
NS={"svg":"http://www.w3.org/2000/svg"}
FENCE=chr(96)*3

def slug(value):
    return re.sub(r"[^\w\s-]","",value.lower(),flags=re.UNICODE).replace(" ","-")

def anchors(path):
    source=re.sub(FENCE+r".*?"+FENCE,"",path.read_text(encoding="utf-8"),flags=re.S)
    found=set();counts={}
    for line in source.splitlines():
        m=re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$",line)
        if m:
            base=slug(m.group(1))
            n=counts.get(base,0);counts[base]=n+1
            found.add(base+(f"-{n}" if n else ""))
    found.update(re.findall(r'\bid=["\']([^"\']+)',source))
    return found

def check():
    issues=[];links=0;images=0;svgs=0
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts:continue
        source=path.read_text(encoding="utf-8")
        if "\u2014" in source:issues.append(f"{path.relative_to(ROOT)}: em dash in prose")
        text=re.sub(FENCE+r".*?"+FENCE,"",source,flags=re.S)
        for m in re.finditer(r'(!?)\[([^\]]*)\]\(([^)\n]+)\)',text):
            image,label,target=m.groups()
            target=target.strip().split(' "')[0].strip("<>")
            if image:
                images+=1
                if len(label.strip())<10:issues.append(f"{path.relative_to(ROOT)}: missing/useful image alt")
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:",target):continue
            parts=urlsplit(target);links+=1
            dest=(path.parent/unquote(parts.path)).resolve() if parts.path else path
            if not dest.is_relative_to(ROOT):
                issues.append(f"{path.relative_to(ROOT)}: link escapes repository: {target}")
            elif not dest.exists():
                issues.append(f"{path.relative_to(ROOT)}: missing {target}")
            elif parts.fragment and dest.suffix.lower()==".md" and unquote(parts.fragment) not in anchors(dest):
                issues.append(f"{path.relative_to(ROOT)}: missing anchor {target}")
    for path in sorted(ROOT.rglob("*.svg")):
        if ".git" in path.parts:continue
        svgs+=1
        try:
            svg=ET.parse(path).getroot()
            view=[float(x) for x in svg.attrib["viewBox"].split()]
            for tag in ["title","desc"]:
                node=svg.find("svg:"+tag,NS)
                if node is None or not (node.text or "").strip():raise ValueError("missing "+tag)
            for node in svg.findall(".//svg:text",NS):
                size=float(node.attrib.get("font-size","0"))
                x,y=float(node.attrib["x"]),float(node.attrib["y"])
                if size<18:raise ValueError("font smaller than 18")
                if not (0<=x<view[2] and 0<=y<view[3]):raise ValueError("text origin outside canvas")
            if svg.findall(".//svg:script",NS):raise ValueError("script in image")
        except (ValueError,KeyError,ET.ParseError) as e:
            issues.append(f"{path.relative_to(ROOT)}: SVG {e}")
    return issues,{"local_links":links,"images":images,"svgs":svgs}

def main():
    issues,counts=check()
    print(counts)
    for issue in issues:print(issue)
    print(f"{len(issues)} issues")
    return bool(issues)

if __name__=="__main__":
    sys.exit(main())

# Visual Quality Control

This repository uses a lightweight quality gate for SVG visuals before they are committed.

The gate is implemented in [`tools/visual_quality_check.py`](../tools/visual_quality_check.py). It checks for structure, readability, metadata, text containment, and arrow-marker integrity. The goal is not to replace human review; the goal is to catch preventable visual issues before the artifacts reach GitHub.

## Gate Checks

- SVG parses as XML.
- SVG includes `title` and `desc` metadata.
- SVG uses a GitHub-friendly `viewBox` of at least 1000 by 600.
- Text elements use readable font sizes.
- Text coordinates stay inside the canvas.
- Card-tagged groups keep text within card boundaries.
- Arrow-tagged paths use a defined arrow marker.

## How To Run

From the repository root:

```powershell
python tools/generate_portfolio_visuals.py --repo-root .
python tools/visual_quality_check.py projects --report project-management/visual-quality-report.md
```

The generated report is stored in [`visual-quality-report.md`](visual-quality-report.md).

## Human Review Notes

The automated gate catches measurable layout risks. A final human review should still check whether the artifact feels clear, restrained, and useful for the reader. Visuals should support the analysis without becoming decorative noise.

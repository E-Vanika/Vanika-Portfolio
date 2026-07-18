#!/usr/bin/env python3
"""Dependency-free quality gate for this static portfolio.

Checks document essentials, in-page anchors, and references to local files. It is
intentionally built with Python's standard library so it runs locally or in CI
without installing packages.
"""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys


class DocumentInspector(HTMLParser):
    """Collect the minimum structural and linking data needed for validation."""

    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.references: list[tuple[str, str]] = []
        self.main_count = 0
        self.title_count = 0
        self.has_viewport = False
        self.images_without_alt: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if "id" in attributes and attributes["id"]:
            self.ids.add(attributes["id"])
        if tag == "main":
            self.main_count += 1
        if tag == "title":
            self.title_count += 1
        if tag == "meta" and attributes.get("name", "").lower() == "viewport":
            self.has_viewport = True
        if tag == "img" and not attributes.get("alt"):
            self.images_without_alt.append(attributes.get("src", "<missing src>"))
        for attribute in ("href", "src"):
            value = attributes.get(attribute)
            if value:
                self.references.append((attribute, value))


def is_external(url: str) -> bool:
    """Return whether a URL is handled by the browser instead of this repository."""
    parsed = urlsplit(url)
    return bool(parsed.scheme) or url.startswith("//")


def validate_document(path: Path, root: Path) -> list[str]:
    """Validate one HTML document and return every human-readable issue."""
    inspector = DocumentInspector()
    inspector.feed(path.read_text(encoding="utf-8"))
    inspector.close()

    issues: list[str] = []
    label = path.relative_to(root).as_posix()
    if inspector.main_count != 1:
        issues.append(f"{label}: expected exactly one <main>, found {inspector.main_count}")
    if inspector.title_count != 1:
        issues.append(f"{label}: expected exactly one <title>, found {inspector.title_count}")
    if not inspector.has_viewport:
        issues.append(f"{label}: missing responsive viewport meta tag")
    for source in inspector.images_without_alt:
        issues.append(f"{label}: image has no alt text ({source})")

    for attribute, reference in inspector.references:
        if is_external(reference):
            continue
        parsed = urlsplit(reference)
        target = unquote(parsed.path)
        fragment = unquote(parsed.fragment)
        target_path = path if not target else root / target.lstrip("/") if target.startswith("/") else path.parent / target

        if target and not target_path.is_file():
            issues.append(f"{label}: {attribute} points to missing file '{reference}'")
            continue
        if fragment:
            anchor_source = target_path if target else path
            anchor_inspector = inspector if anchor_source == path else DocumentInspector()
            if anchor_source != path and anchor_source.suffix == ".html" and anchor_source.is_file():
                anchor_inspector.feed(anchor_source.read_text(encoding="utf-8"))
            if fragment not in anchor_inspector.ids:
                issues.append(f"{label}: link points to missing anchor '#{fragment}'")
    return issues


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    html_files = sorted(root.rglob("*.html"))
    if not html_files:
        print("ERROR: No HTML files found.")
        return 1

    issues = [issue for file_path in html_files for issue in validate_document(file_path, root)]
    if issues:
        print("Static-site validation failed:")
        print("\n".join(f"- {issue}" for issue in issues))
        return 1

    print(f"Static-site validation passed: {len(html_files)} HTML file(s) checked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

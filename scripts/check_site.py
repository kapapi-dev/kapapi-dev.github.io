"""Validate the committed static site without third-party dependencies."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.html_lang = ""
        self.title_depth = 0
        self.title = ""
        self.h1_count = 0
        self.description = ""
        self.canonical = ""
        self.references: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "html":
            self.html_lang = values.get("lang") or ""
        elif tag == "title":
            self.title_depth += 1
        elif tag == "h1":
            self.h1_count += 1
        elif tag == "meta" and values.get("name", "").lower() == "description":
            self.description = values.get("content") or ""
        elif tag == "link" and values.get("rel", "").lower() == "canonical":
            self.canonical = values.get("href") or ""

        if tag in {"a", "link"} and values.get("href"):
            self.references.append(values["href"] or "")
        if tag in {"img", "script"} and values.get("src"):
            self.references.append(values["src"] or "")

    def handle_endtag(self, tag: str) -> None:
        if tag == "title" and self.title_depth:
            self.title_depth -= 1

    def handle_data(self, data: str) -> None:
        if self.title_depth:
            self.title += data


def resolve_internal(reference: str) -> Path | None:
    if reference.startswith(("#", "mailto:", "tel:", "data:")):
        return None
    parsed = urlsplit(reference)
    if parsed.scheme or parsed.netloc:
        return None
    path = unquote(parsed.path)
    if not path:
        return None
    candidate = ROOT / path.lstrip("/")
    if path.endswith("/") or candidate.is_dir():
        candidate /= "index.html"
    return candidate


def main() -> None:
    errors: list[str] = []
    pages = sorted(ROOT.rglob("*.html"))
    if not pages:
        errors.append("No HTML pages found")

    for page in pages:
        relative = page.relative_to(ROOT).as_posix()
        source = page.read_text(encoding="utf-8")
        parser = PageParser()
        parser.feed(source)

        if parser.html_lang != "en":
            errors.append(f"{relative}: expected html lang=en")
        if not parser.title.strip():
            errors.append(f"{relative}: missing title")
        if parser.h1_count != 1:
            errors.append(f"{relative}: expected one h1, found {parser.h1_count}")
        if not parser.description.strip():
            errors.append(f"{relative}: missing meta description")
        if page.name != "404.html" and not parser.canonical.startswith("https://kapapi.dev/"):
            errors.append(f"{relative}: missing kapapi.dev canonical")
        if "__" in source:
            errors.append(f"{relative}: unresolved template placeholder")

        for reference in parser.references:
            target = resolve_internal(reference)
            if target is not None and not target.is_file():
                errors.append(f"{relative}: broken internal reference {reference}")

    sitemap = ROOT / "sitemap.xml"
    try:
        locations = {
            node.text
            for node in ET.parse(sitemap).iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")
        }
    except (ET.ParseError, OSError) as error:
        errors.append(f"sitemap.xml: {error}")
        locations = set()
    required_sendarc_urls = {
        "https://kapapi.dev/sendarc/",
        "https://kapapi.dev/sendarc/privacy.html",
        "https://kapapi.dev/sendarc/terms.html",
        "https://kapapi.dev/sendarc/support.html",
    }
    for required_url in sorted(required_sendarc_urls):
        if required_url not in locations:
            errors.append(f"sitemap.xml: missing {required_url}")

    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Validated {len(pages)} HTML pages and {len(locations)} sitemap URLs")


if __name__ == "__main__":
    main()

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"


class Inspector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.links = []
        self.h1_count = 0
        self.lang = None
        self.has_main = False
        self.has_description = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "html":
            self.lang = attrs.get("lang")
        if tag == "h1":
            self.h1_count += 1
        if tag == "main":
            self.has_main = True
        if tag == "meta" and attrs.get("name") == "description" and attrs.get("content"):
            self.has_description = True
        if attrs.get("id"):
            self.ids.append(attrs["id"])
        if tag in {"a", "link", "script"}:
            target = attrs.get("href") or attrs.get("src")
            if target:
                self.links.append(target)


def target_path(source: Path, target: str) -> Path | None:
    parsed = urlparse(target)
    if parsed.scheme or target.startswith(("mailto:", "tel:", "#")):
        return None
    clean = parsed.path
    if not clean:
        return None
    path = (SITE / clean.lstrip("/")) if clean.startswith("/") else (source.parent / clean)
    if clean.endswith("/"):
        path /= "index.html"
    return path.resolve()


errors = []
html_files = sorted(SITE.rglob("*.html"))
if len(html_files) < 8:
    errors.append(f"Expected at least 8 HTML pages; found {len(html_files)}")

for page in html_files:
    text = page.read_text(encoding="utf-8")
    parser = Inspector()
    parser.feed(text)
    if parser.lang != "en-CA":
        errors.append(f"{page}: missing lang=en-CA")
    if parser.h1_count != 1:
        errors.append(f"{page}: expected exactly one h1, found {parser.h1_count}")
    if not parser.has_main:
        errors.append(f"{page}: missing main landmark")
    if not parser.has_description:
        errors.append(f"{page}: missing description")
    duplicates = sorted({item for item in parser.ids if parser.ids.count(item) > 1})
    if duplicates:
        errors.append(f"{page}: duplicate ids {duplicates}")
    for link in parser.links:
        target = target_path(page, link)
        if target is not None and not target.exists():
            errors.append(f"{page}: missing local target for {link} ({target})")
    for stale in ("not licensed by the Government of Ontario", "Opening Sept 2025", "7am - 6pm"):
        if stale.casefold() in text.casefold():
            errors.append(f"{page}: contains stale wording {stale!r}")

if errors:
    raise SystemExit("\n".join(errors))

print(f"Checked {len(html_files)} HTML pages; all local links and structural checks passed.")

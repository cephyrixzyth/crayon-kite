"""Check the exact static artifact that GitHub Pages uploads."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1] / 'dist'


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.ids = set()
        self.title_parts = []
        self.in_sheet_title = False
        self.selected_art = {}
        self.references = []
        self.sheets = []
        self.feed(path.read_text(encoding='utf-8'))

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if 'id' in attrs:
            if attrs['id'] in self.ids:
                raise ValueError(f'{self.path}: duplicate ID {attrs["id"]}')
            self.ids.add(attrs['id'])
        for attribute in ('href', 'src'):
            if attrs.get(attribute):
                self.references.append(attrs[attribute])
        if 'srcset' in attrs:
            self.references.extend(part.strip().split()[0] for part in attrs['srcset'].split(','))
        if tag == 'h1' and attrs.get('id') == 'selected-title':
            self.in_sheet_title = True
        if tag == 'img' and attrs.get('id') == 'selected-art':
            self.selected_art = attrs
        if 'data-file' in attrs:
            self.sheets.append(attrs)

    def handle_data(self, text):
        if self.in_sheet_title:
            self.title_parts.append(text)

    def handle_endtag(self, tag):
        if tag == 'h1':
            self.in_sheet_title = False


def check():
    pages = {path: Page(path) for path in ROOT.rglob('*.html')}
    for path, page in pages.items():
        for reference in page.references:
            url = urlsplit(reference)
            if url.scheme or url.netloc:
                continue
            raw = unquote(url.path)
            target = ((ROOT / raw.lstrip('/')) if raw.startswith('/') else path.parent / raw) if raw else path
            if target.is_dir():
                target = target / 'index.html'
            target = target.resolve()
            if ROOT not in target.parents or not target.is_file():
                raise ValueError(f'{path.relative_to(ROOT)}: missing {reference}')
            if url.fragment and target in pages and '=' not in url.fragment:
                if unquote(url.fragment) not in pages[target].ids:
                    raise ValueError(f'{path.relative_to(ROOT)}: missing fragment {reference}')

    hub = ROOT / 'budgie-adventures/index.html'
    sheets = pages[hub].sheets
    if len(sheets) != 10 or len({s['data-id'] for s in sheets}) != len(sheets):
        raise ValueError('Expected ten unique activities on the coloring shelf')
    for sheet in sheets:
        slug = sheet['data-id']
        detail = pages[(hub.parent / sheet['href']).resolve()]
        image_file = Path(detail.selected_art.get('src', '')).name
        identity = (''.join(detail.title_parts).strip(), image_file, detail.selected_art.get('alt'))
        expected = (sheet['data-title'], sheet['data-file'], sheet['data-alt'])
        if identity != expected:
            raise ValueError(f'{slug}: printable page differs from its shelf entry')
        if not (ROOT / 'assets/sheet-previews' / (slug + '.webp')).is_file():
            raise ValueError(f'{slug}: missing small preview')
    if (ROOT / 'CNAME').read_text().strip() != 'crayonkite.com':
        raise ValueError('Unexpected Pages custom domain')
    print(f'Validated {len(pages)} HTML pages, {sum(len(p.references) for p in pages.values())} internal and external references inspected, and {len(sheets)} printable records.')


if __name__ == '__main__':
    check()

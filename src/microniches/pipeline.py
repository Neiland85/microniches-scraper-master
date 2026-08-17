from .collector import fetch_html
from .models import PageSnapshot
from .parser import parse_page


def collect_page(url: str, **collector_options: object) -> PageSnapshot:
    status_code, html = fetch_html(url, **collector_options)
    return parse_page(url, status_code, html)

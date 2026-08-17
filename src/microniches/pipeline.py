from __future__ import annotations

import hashlib
from datetime import datetime, timezone

from .collector import fetch_html
from .models import CollectionResult
from .parser import parse_page


def collect_page(url: str, **collector_options: object) -> CollectionResult:
    status_code, html, final_url = fetch_html(url, **collector_options)

    snapshot = parse_page(url, status_code, html)

    return CollectionResult(
        snapshot=snapshot,
        final_url=final_url,
        collected_at=datetime.now(timezone.utc),
        content_sha256=hashlib.sha256(html.encode("utf-8")).hexdigest(),
    )

from __future__ import annotations

import time
from collections.abc import Callable

import httpx


class CollectionError(RuntimeError):
    """Raised when a page cannot be collected within the configured policy."""


def fetch_html(
    url: str,
    *,
    timeout: float = 10.0,
    max_retries: int = 2,
    backoff: float = 0.5,
    sleep: Callable[[float], None] = time.sleep,
) -> tuple[int, str]:
    """Fetch a page with bounded retries for transient upstream failures.

    This collector intentionally does not attempt to bypass access controls,
    CAPTCHAs, WAFs, authentication, or anti-bot mechanisms.
    """
    last_error: Exception | None = None

    with httpx.Client(
        timeout=timeout,
        follow_redirects=True,
        headers={"User-Agent": "microniches-scraper-master/0.1"},
    ) as client:
        for attempt in range(max_retries + 1):
            try:
                response = client.get(url)
                if response.status_code in {408, 429} or 500 <= response.status_code < 600:
                    if attempt < max_retries:
                        sleep(backoff * (2**attempt))
                        continue
                response.raise_for_status()
                return response.status_code, response.text
            except (httpx.HTTPError, httpx.TimeoutException) as exc:
                last_error = exc
                if attempt < max_retries:
                    sleep(backoff * (2**attempt))
                    continue
                break

    raise CollectionError(f"Unable to collect {url!r}") from last_error

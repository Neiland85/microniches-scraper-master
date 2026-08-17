# Microniches Scraper Master

A small Python data-acquisition prototype evolved from an earlier SEO/scraping experiment.

## Current scope

The modernized core separates:

- HTTP collection with bounded timeouts and retries;
- HTML parsing;
- a normalized `PageSnapshot` data contract;
- a `CollectionResult` carrying final URL, UTC collection time and content SHA-256;
- a small composition pipeline;
- tests for parsing and retry behavior.

The collector deliberately does **not** attempt to bypass authentication, CAPTCHAs, WAFs, anti-bot controls, or other access restrictions. Collection policy is part of the system boundary.

## Development

Requires Python 3.11+.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[test]'
pytest
```

Example:

```python
from microniches.pipeline import collect_page

result = collect_page("https://example.com")
print(result.snapshot)
print(result.final_url)
print(result.collected_at)
print(result.content_sha256)
```

## Architecture

```text
URL
  -> Collector
  -> HTML
  -> Parser
  -> PageSnapshot contract
  -> CollectionResult
  -> Consumer / export
```

The design keeps collection policy independent from parsing and downstream consumers. This makes retry behavior, parser correctness and data contracts independently testable.

## Historical context

The repository contains the original prototype history. Earlier versions combined `requests`, BeautifulSoup and `pytrends`, and introduced explicit handling for upstream rate limiting. The current implementation is a deliberately small modernization of the legitimate data-acquisition core rather than a claim of distributed scraping at industrial scale.

## Responsible use

Only collect data where the access method and intended use are permitted. Respect applicable terms, robots policies where relevant, rate limits, privacy requirements and other access controls.

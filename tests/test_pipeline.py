import hashlib

import httpx

from microniches.pipeline import collect_page


def test_collect_page_produces_verifiable_result(monkeypatch) -> None:
    html = """
    <html>
      <head>
        <title>Example</title>
        <meta name="description" content="A page">
      </head>
    </html>
    """

    response = httpx.Response(
        200,
        text=html,
        request=httpx.Request("GET", "https://example.com"),
    )

    class FakeClient:
        def __init__(self, **_: object) -> None:
            pass

        def __enter__(self) -> "FakeClient":
            return self

        def __exit__(self, *_: object) -> None:
            return None

        def get(self, _: str) -> httpx.Response:
            return response

    monkeypatch.setattr("microniches.collector.httpx.Client", FakeClient)

    result = collect_page("https://example.com")

    assert result.snapshot.ok
    assert result.snapshot.title == "Example"
    assert result.final_url == "https://example.com"
    assert result.collected_at.tzinfo is not None
    assert result.collected_at.utcoffset().total_seconds() == 0
    assert result.content_sha256 == hashlib.sha256(
        html.encode("utf-8")
    ).hexdigest()

import httpx
import pytest

from microniches.collector import CollectionError, fetch_html


def test_fetch_html_retries_transient_status(monkeypatch: pytest.MonkeyPatch) -> None:
    responses = iter(
        [
            httpx.Response(
                429,
                request=httpx.Request("GET", "https://example.com"),
            ),
            httpx.Response(
                200,
                text="ok",
                request=httpx.Request("GET", "https://example.com"),
            ),
        ]
    )

    class FakeClient:
        def __init__(self, **_: object) -> None:
            pass

        def __enter__(self) -> "FakeClient":
            return self

        def __exit__(self, *_: object) -> None:
            return None

        def get(self, _: str) -> httpx.Response:
            return next(responses)

    monkeypatch.setattr("microniches.collector.httpx.Client", FakeClient)

    status, body, final_url = fetch_html(
        "https://example.com",
        backoff=0,
        sleep=lambda _: None,
    )

    assert status == 200
    assert body == "ok"
    assert final_url == "https://example.com"


def test_fetch_html_raises_after_retry_budget(monkeypatch: pytest.MonkeyPatch) -> None:
    response = httpx.Response(
        503,
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

    with pytest.raises(CollectionError):
        fetch_html(
            "https://example.com",
            max_retries=1,
            backoff=0,
            sleep=lambda _: None,
        )

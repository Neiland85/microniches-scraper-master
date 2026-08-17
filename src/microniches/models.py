from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class PageSnapshot:
    url: str
    title: str | None
    description: str | None
    keywords: str | None
    status_code: int

    @property
    def ok(self) -> bool:
        return 200 <= self.status_code < 300

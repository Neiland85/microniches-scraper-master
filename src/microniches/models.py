from dataclasses import dataclass
from datetime import datetime


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


@dataclass(frozen=True, slots=True)
class CollectionResult:
    snapshot: PageSnapshot
    final_url: str
    collected_at: datetime
    content_sha256: str

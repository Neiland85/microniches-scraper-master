from bs4 import BeautifulSoup

from .models import PageSnapshot


def parse_page(url: str, status_code: int, html: str) -> PageSnapshot:
    soup = BeautifulSoup(html, "html.parser")
    title = soup.title.get_text(strip=True) if soup.title else None

    description_tag = soup.find("meta", attrs={"name": "description"})
    description = description_tag.get("content") if description_tag else None

    keywords_tag = soup.find("meta", attrs={"name": "keywords"})
    keywords = keywords_tag.get("content") if keywords_tag else None

    return PageSnapshot(
        url=url,
        title=title,
        description=description,
        keywords=keywords,
        status_code=status_code,
    )

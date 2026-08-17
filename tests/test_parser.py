from microniches.parser import parse_page


def test_parse_page_normalizes_seo_metadata() -> None:
    html = """
    <html>
      <head>
        <title>Example</title>
        <meta name="description" content="A page">
        <meta name="keywords" content="one,two">
      </head>
    </html>
    """

    result = parse_page("https://example.com", 200, html)

    assert result.ok
    assert result.title == "Example"
    assert result.description == "A page"
    assert result.keywords == "one,two"

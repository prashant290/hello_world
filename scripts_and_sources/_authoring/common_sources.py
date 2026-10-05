"""Helper for authoring files."""
def S(authors, year, title, venue, url, verified):
    return dict(authors=authors, year=year, title=title, venue=venue, url=url, verified=verified)

SEC = "web search 2026-10-05: citation + abstract/findings confirmed from publisher/database page quoted in search results"
SECOND = "web search 2026-10-05: citation confirmed; specific figures confirmed from secondary summaries that quote the paper (primary PDF not directly readable from this environment)"

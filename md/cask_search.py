#!/usr/bin/env python3
"""
Cask Search - Free web search via local SearXNG
Usage: python3 cask_search.py "your query" [--limit 5]

Returns JSON array: [{"title": "...", "url": "...", "content": "..."}]
"""

import json, sys, urllib.request, urllib.parse, urllib.error

SEARXNG_URL = "http://localhost:8888"

def search(query: str, limit: int = 5) -> list:
    """Search the web using local SearXNG instance. Returns list of results."""
    params = urllib.parse.urlencode({
        "q": query,
        "format": "json",
        "categories": "general,news"
    })
    url = f"{SEARXNG_URL}/search?{params}"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36"}
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        return [{"title": f"HTTP {e.code}: {e.reason}", "url": "", "content": f"Error searching for: {query}"}]
    except Exception as e:
        return [{"title": f"Search error: {e}", "url": "", "content": ""}]

    results = data.get("results", [])
    return [
        {
            "title": r.get("title", ""),
            "url": r.get("url", ""),
            "content": r.get("content", "")[:300],
        }
        for r in results[:limit]
    ]


if __name__ == "__main__":
    args = sys.argv[1:]
    query_parts = []
    limit = 5
    skip_next = False
    for i, a in enumerate(args):
        if skip_next:
            skip_next = False
            continue
        if a == "--limit" and i + 1 < len(args):
            limit = int(args[i + 1])
            skip_next = True
        else:
            query_parts.append(a)

    query = " ".join(query_parts)
    results = search(query, limit)
    print(json.dumps(results, indent=2, ensure_ascii=False))

"""Optional Tavily web-search tool (falls back gracefully without a key)."""
import os
from langchain.tools import tool

@tool
def search_satellite_news(query: str) -> str:
    """Search the web for recent satellite/mission news. Use for current information
    not in the internal database."""
    if not os.getenv("TAVILY_API_KEY"):
        return "Web search unavailable (no TAVILY_API_KEY). Rely on the database."
    from tavily import TavilyClient
    res = TavilyClient(api_key=os.getenv("TAVILY_API_KEY")).search(query, max_results=3)
    return "\n".join(f"- {r['title']}: {r['content'][:200]}" for r in res["results"])

"""Shopper agent: Tavily search tool + ReAct reasoning."""
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain.tools import tool
from langchain import hub

load_dotenv()

@tool
def web_product_search(query: str) -> str:
    """Search the live web for products, prices, and reviews. Use to find current
    options for a shopping query. Returns titles + snippets."""
    if not os.getenv("TAVILY_API_KEY"):
        return "Search unavailable (no TAVILY_API_KEY)."
    from tavily import TavilyClient
    res = TavilyClient(api_key=os.getenv("TAVILY_API_KEY")).search(query, max_results=5)
    return "\n".join(f"- {r['title']}: {r['content'][:200]} ({r['url']})"
                     for r in res["results"])

def build_agent(verbose: bool = False) -> AgentExecutor:
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    tools = [web_product_search]
    agent = create_react_agent(llm, tools, hub.pull("hwchase17/react"))
    return AgentExecutor(agent=agent, tools=tools, verbose=verbose,
                         max_iterations=8, handle_parsing_errors=True)

if __name__ == "__main__":
    ex = build_agent(verbose=True)
    print(ex.invoke({"input": "best budget mechanical keyboard under $80, ranked"})["output"])

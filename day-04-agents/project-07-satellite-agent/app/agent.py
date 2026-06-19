"""Assemble the ReAct agent from the tools."""
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub
from app.tools.satellite_tools import lookup_satellite_database, calculate_orbital_params
from app.tools.search_tools import search_satellite_news
from app.tools.report_tools import compile_satellite_report

load_dotenv()

def build_agent(verbose: bool = False) -> AgentExecutor:
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    tools = [lookup_satellite_database, calculate_orbital_params,
             search_satellite_news, compile_satellite_report]
    prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm, tools, prompt)
    return AgentExecutor(agent=agent, tools=tools, verbose=verbose,
                         max_iterations=10, handle_parsing_errors=True)

if __name__ == "__main__":
    ex = build_agent(verbose=True)
    out = ex.invoke({"input": "Build an intelligence report on the ISS, including its orbit."})
    print("\nFINAL:\n", out["output"])

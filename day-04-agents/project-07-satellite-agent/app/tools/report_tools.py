"""Format the gathered facts into a structured intelligence report."""
from langchain.tools import tool

@tool
def compile_satellite_report(facts: str) -> str:
    """Format collected satellite facts into a clean report. Call LAST, once you have
    database info (and any news). Input: the facts gathered so far."""
    bar = "=" * 52
    return f"{bar}\nSATELLITE INTELLIGENCE REPORT\n{bar}\n{facts}\n{bar}"

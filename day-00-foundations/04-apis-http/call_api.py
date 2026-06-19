"""Call a public REST API. Requires: pip install requests"""
import requests
r = requests.get("https://api.github.com/repos/langchain-ai/langgraph", timeout=10)
r.raise_for_status()
d = r.json()
print("Repo:", d["full_name"], "| Stars:", d["stargazers_count"])
print("Description:", d["description"])

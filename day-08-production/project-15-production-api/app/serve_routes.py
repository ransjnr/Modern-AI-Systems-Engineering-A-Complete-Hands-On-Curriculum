"""Mount a chain via LangServe onto the same app."""
from langserve import add_routes
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from app.main import app
from app.config import settings

chain = (ChatPromptTemplate.from_template("Answer concisely: {question}")
         | ChatOpenAI(model=settings.model, temperature=0))
add_routes(app, chain, path="/chat")

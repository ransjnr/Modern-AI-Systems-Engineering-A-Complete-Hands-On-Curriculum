"""Load test. Run: locust -f locustfile.py --host http://localhost:8013"""
from locust import HttpUser, task, between
import random

QUESTIONS = [
    "What is a vector database?", "What is a vector DB?",   # paraphrase -> semantic
    "Explain RAG in one sentence.", "What does LoRA do?",
]

class ApiUser(HttpUser):
    wait_time = between(0.1, 0.5)
    @task
    def ask(self):
        self.client.post("/ask", json={"question": random.choice(QUESTIONS)})

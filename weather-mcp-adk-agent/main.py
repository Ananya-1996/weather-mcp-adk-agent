from fastapi import FastAPI
from adk_agent.weather_app.agent import run_agent

app = FastAPI()

@app.get("/")
def home():
    return {"message": "MCP ADK Agent Running"}

@app.get("/ask")
def ask(query: str):
    return {"query": query, "response": run_agent(query)}

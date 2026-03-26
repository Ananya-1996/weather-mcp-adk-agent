from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from agent import run_agent

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Sales AI Agent Running 🚀"}


@app.get("/ask", response_class=HTMLResponse)
def ask(query: str):
    result = run_agent(query)

    return f"""
    <html>
    <head>
        <title>Smart Sales Meeting Assistant</title>
    </head>
    <body style="font-family: Arial, sans-serif; background-color:#f5f7fa; padding:40px;">

        <div style="max-width:700px; margin:auto; background:white; padding:25px; border-radius:12px; box-shadow:0 4px 12px rgba(0,0,0,0.1);">

            <h2 style="color:#2c3e50;">🤖 Smart Sales Meeting Assistant</h2>

            <p><b>Query:</b> {query}</p>

            <hr style="margin:20px 0;"/>

            <div style="white-space: pre-line; font-size:16px; color:#333;">
                {result}
            </div>

        </div>

    </body>
    </html>
    """

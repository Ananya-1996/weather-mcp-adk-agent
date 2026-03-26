from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi import Query
from adk_agent.weather_app.agent import run_agent

app = FastAPI()


# ✅ Chat UI (Sales AI Assistant)
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <head>
        <title>Sales AI Assistant</title>
        <style>
            body {
                font-family: Arial;
                background: #0f172a;
                color: white;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .chat-container {
                width: 420px;
                background: #1e293b;
                border-radius: 12px;
                padding: 15px;
                box-shadow: 0px 0px 15px rgba(0,0,0,0.6);
            }
            .messages {
                height: 420px;
                overflow-y: auto;
                margin-bottom: 10px;
                padding: 5px;
            }
            .msg {
                margin: 8px 0;
                padding: 10px;
                border-radius: 8px;
                max-width: 80%;
            }
            .user {
                background: #3b82f6;
                text-align: right;
                margin-left: auto;
            }
            .bot {
                background: #334155;
                text-align: left;
                margin-right: auto;
            }
            input {
                width: 70%;
                padding: 10px;
                border-radius: 5px;
                border: none;
                outline: none;
            }
            button {
                padding: 10px;
                border: none;
                background: #22c55e;
                color: white;
                border-radius: 5px;
                cursor: pointer;
            }
        </style>
    </head>

    <body>
        <div class="chat-container">
            <h2>🤖 Sales AI Assistant</h2>

            <div id="messages" class="messages"></div>

            <input id="query" placeholder="Ask sales insights..." />
            <button onclick="sendMessage()">Send</button>
        </div>

        <script>
            async function sendMessage() {
                let input = document.getElementById("query");
                let message = input.value;

                if (!message) return;

                let messagesDiv = document.getElementById("messages");

                // user message
                messagesDiv.innerHTML += `<div class="msg user">${message}</div>`;

                input.value = "";

                // call backend
                let response = await fetch(`/ask?query=${encodeURIComponent(message)}`);
                let data = await response.json();

                // bot message
                messagesDiv.innerHTML += `<div class="msg bot">${data.response}</div>`;

                messagesDiv.scrollTop = messagesDiv.scrollHeight;
            }
        </script>
    </body>
    </html>
    """


# ✅ Backend API
@app.get("/ask")
def ask(query: str = Query(...)):
    result = run_agent(query)  # ✅ no await
    return {"response": result}

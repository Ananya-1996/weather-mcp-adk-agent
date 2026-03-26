# 🤖 Sales AI Assistant (GenAI + FastAPI + Cloud Run)

A modern **AI-powered Sales Assistant** built using FastAPI and deployed on Google Cloud Run.
It provides intelligent responses to sales-related queries through a sleek chat-based UI.

---

## 🚀 Features

* 💬 ChatGPT-style UI for interactive conversations
* 🤖 AI-powered responses using GenAI agent
* ⚡ FastAPI backend (high performance)
* ☁️ Deployed on Google Cloud Run
* 🎯 Sales-focused query handling (strategy, leads, conversion, outreach)

---

## 🧠 Use Cases

* 📊 Sales strategy recommendations
* 📈 Conversion rate optimization tips
* 📞 Cold outreach guidance
* 🧾 Lead qualification insights
* 🏢 CRM & pipeline suggestions

---

## 🏗️ Tech Stack

* **Backend:** FastAPI (Python)
* **Frontend:** HTML, CSS, JavaScript (Chat UI)
* **AI Layer:** Custom Agent (ADK / GenAI)
* **Deployment:** Google Cloud Run
* **Language:** Python 3.10+

---

## 📁 Project Structure

```
weather-mcp-adk-agent/
│── main.py
│── run_agent.py
│── requirements.txt
│── adk_agent/
│   ├── __init__.py
│   └── weather_app/
│       ├── __init__.py
│       ├── agent.py
│       └── tools.py
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd weather-mcp-adk-agent
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run Locally

```bash
uvicorn main:app --reload
```

Open:

```
http://127.0.0.1:8000
```

---

## ☁️ Deployment (Google Cloud Run)

### Step 1: Authenticate

```bash
gcloud auth login
gcloud config set project <your-project-id>
```

---

### Step 2: Deploy

```bash
gcloud run deploy weather-agent \
  --source . \
  --region us-central1 \
  --allow-unauthenticated
```

---

## 🌐 API Endpoints

| Endpoint         | Method | Description                  |
| ---------------- | ------ | ---------------------------- |
| `/`              | GET    | Chat UI (Sales AI Assistant) |
| `/ask?query=...` | GET    | Returns AI response          |

---

## 🖥️ Demo

👉 Open the deployed URL and start chatting with the AI assistant.

Example Queries:

* “Best sales strategy for startups”
* “How to increase B2B conversion rate”
* “Cold email tips for SaaS”

---

## ⚠️ Troubleshooting

### ❌ ModuleNotFoundError

* Ensure correct import path:

```python
from adk_agent.weather_app.agent import run_agent
```

### ❌ Cloud Run not starting

* Check logs:

```bash
gcloud logs read
```

### ❌ Async error (`await`)

* Remove `await` if function is not async

---

## 📌 Future Enhancements

* 📊 Sales dashboard with analytics
* 🧠 Context memory (conversation history)
* 🔄 Streaming responses (typing effect)
* 🎨 Advanced UI with Tailwind / React
* 🔗 CRM integrations (Salesforce, HubSpot)

---

## 👩‍💻 Author

**Ananya Shetty**

* B.Com Final Year | GenAI Enthusiast
* Focus: AI + Business + Product Development

---

## ⭐ Contribute

Feel free to fork, improve, and submit PRs 🚀

---

## 📜 License

This project is for learning and demonstration purposes.

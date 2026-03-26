# 🌦 Smart Meeting Scheduler Agent (ADK + MCP)

## 🚀 Live Demo

👉 https://weather-agent-593321241935.us-central1.run.app/ask?query=schedule meeting in bangalore

---

## 🧠 Overview

This project implements an **AI agent using Google ADK and the Model Context Protocol (MCP)** to integrate external data and generate intelligent decisions.

The agent:

* Connects to a real-time **weather API**
* Retrieves structured data via MCP tools
* Uses the data to recommend **online or offline meetings**
* Provides **clear, explainable reasoning**

---

## 🎯 Problem Statement

Build an AI agent that:

* Uses MCP to connect to an external tool
* Retrieves structured data
* Uses that data to generate a response
* Is implemented using ADK
* Is deployed and accessible via Cloud Run

---

## ✅ Solution

This project satisfies all requirements by:

* Implementing an **ADK-based agent (`LlmAgent`)**
* Using **MCPToolset** to integrate an external weather API
* Retrieving structured weather data (temperature, conditions)
* Applying reasoning logic to generate actionable insights
* Deploying the solution on **Google Cloud Run**

---

## 🔌 MCP Tool Integration

### Tool: `get_weather(city)`

* Connects to **OpenWeatherMap API**
* Returns structured JSON:

```json
{
  "city": "Bangalore",
  "temperature": 28,
  "condition": "clear sky"
}
```

### MCP Flow

User → Agent → MCP Tool → External API → Structured Data → Decision → Response

---

## 🏗 Architecture

```
User Request
     ↓
FastAPI (Cloud Run)
     ↓
ADK Agent (LlmAgent)
     ↓
MCP Tool (Weather)
     ↓
External API (OpenWeather)
     ↓
Structured Data
     ↓
Decision Logic
     ↓
Final Response
```

---

## ✨ Features

* 🔌 MCP-based tool integration
* 🤖 ADK agent architecture
* 🌐 Real-time external API usage
* 🧠 Context-aware decision making
* 📊 Structured & explainable output
* ☁️ Cloud-native deployment (Cloud Run)

---

## 💡 Use Case

This agent helps users:

* Decide whether to hold **online or offline meetings**
* Choose **optimal meeting conditions**
* Make **data-driven scheduling decisions**

---

## ⚙️ Tech Stack

* Python
* FastAPI
* Google ADK
* MCP Toolset
* OpenWeatherMap API
* Google Cloud Run

---

## 🧪 Example Query

```
/ask?query=schedule meeting in bangalore
```

### Example Output

```
📍 Location: Bangalore

🌦 Weather:
- Temperature: 32°C
- Condition: scattered clouds

🧠 Decision:
→ ONLINE meeting recommended

📌 Reason:
Unfavorable weather conditions
```

---

## 🚀 How to Run Locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

---

## 🔑 Environment Variables

Set your API key:

```bash
export WEATHER_API_KEY=your_openweather_api_key
```

---

## 🏆 Key Highlights

* Demonstrates **MCP-based agent design**
* Uses **real external data**
* Produces **actionable, explainable insights**
* Handles **real-world constraints (model access limitations)** gracefully

---

## 🎤 Submission Statement

> I built an AI agent using Google ADK and MCP Toolset to integrate an external weather API. The agent retrieves structured data and applies reasoning to recommend meeting types. The system is deployed on Cloud Run and demonstrates how agents can convert real-time data into actionable insights.

---

## 🙌 Conclusion

This project showcases how **AI agents can move beyond simple responses** and instead provide **context-aware, data-driven decisions** using MCP-based integrations.

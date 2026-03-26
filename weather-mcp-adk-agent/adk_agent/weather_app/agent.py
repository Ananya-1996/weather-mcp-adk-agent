from adk_agent.weather_app import tools

class WeatherAgent:
    def __init__(self):
        self.name = "weather_agent"
        self.description = "AI agent for smart meeting scheduling using MCP tools"

    def extract_city(self, query: str):
        words = query.lower().split()
        for i, word in enumerate(words):
            if word == "in" and i + 1 < len(words):
                return words[i + 1]
        return words[-1]

    def run(self, query: str):
        try:
            city = self.extract_city(query)

            weather = tools.get_weather(city)
            calendar = tools.get_calendar()

            if "error" in weather:
                return "❌ City not found. Please try again."

            temperature = weather.get("temperature", 0)
            windspeed = weather.get("windspeed", 0)

            free_slots = [t for t, s in calendar.items() if s == "free"]

            if not free_slots:
                return "⚠️ No available time slots."

            is_future = "tomorrow" in query.lower()

            if temperature > 30 or windspeed > 15:
                meeting_type = "online"
                reason = "unfavorable weather conditions (high temperature or wind)"
            else:
                meeting_type = "offline"
                reason = "pleasant weather conditions"

            best_time = free_slots[0]

            return f"""
📍 Location: {city.capitalize()}

🌦 Weather Details:
- Temperature: {temperature}°C
- Wind Speed: {windspeed} km/h

📅 Available Time Slots:
{', '.join(free_slots)}

🧠 Decision:
Based on the weather, an **{meeting_type.upper()} meeting** is recommended.

📌 Reason:
{reason}

⏰ Suggested Time:
{best_time}

{'📅 Note: This recommendation considers future conditions.' if is_future else ''}
"""

        except Exception as e:
            return f"Error: {str(e)}"

root_agent = WeatherAgent()

def run_agent(query: str):
    return root_agent.run(query)

import streamlit as st
import requests

API_KEY = "63b640576bbf3bc58435209eace416db"
BASE_URL = "http://api.openweathermap.org/data/2.5/"


def get_weather(city):
    url = f"{BASE_URL}weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

def get_forecast(city):
    url = f"{BASE_URL}forecast?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else None

st.title("🌤️ Weather Dashboard")
city = st.text_input("Enter city name:", "London")

if st.button("Get Weather"):
    weather_data = get_weather(city)
    forecast_data = get_forecast(city)
    
    if not weather_data or not forecast_data:
        st.error("City not found or API error")
    else:
        st.write(f"### {weather_data['name']}")
        st.write(f"🌡️ Temperature: {weather_data['main']['temp']}°C")
        st.write(f"☁️ Description: {weather_data['weather'][0]['description']}")
        st.write(f"💧 Humidity: {weather_data['main']['humidity']}%")

        st.write("### 5-Day Forecast")
        for item in forecast_data["list"]:
            if "12:00:00" in item["dt_txt"]:
                st.write(f"📅 {item['dt_txt'].split(' ')[0]} - {item['main']['temp']}°C, {item['weather'][0]['description']}")



# def get_weather(city):
#     """Fetch current weather data for a city."""
#     url = f"{BASE_URL}weather?q={city}&appid={API_KEY}&units=metric"
#     response = requests.get(url)
#     return response.json() if response.status_code == 200 else None

# def get_forecast(city):
#     """Fetch 5-day weather forecast for a city."""
#     url = f"{BASE_URL}forecast?q={city}&appid={API_KEY}&units=metric"
#     response = requests.get(url)
#     return response.json() if response.status_code == 200 else None

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/weather", methods=["POST"])
# def weather():
#     city = request.form.get("city")
#     weather_data = get_weather(city)
#     forecast_data = get_forecast(city)
    
#     if not weather_data or not forecast_data:
#         return jsonify({"error": "City not found or API error"}), 404
    
#     return jsonify({
#         "current": {
#             "city": weather_data["name"],
#             "temperature": weather_data["main"]["temp"],
#             "description": weather_data["weather"][0]["description"],
#             "humidity": weather_data["main"]["humidity"]
#         },
#         "forecast": [
#             {
#                 "date": item["dt_txt"],
#                 "temperature": item["main"]["temp"],
#                 "description": item["weather"][0]["description"]
#             }
#             for item in forecast_data["list"] if "12:00:00" in item["dt_txt"]
#         ]
#     })

# if __name__ == "__main__":
#     app.run(debug=True)

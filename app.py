import requests

def get_weather(city, api_key):
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data.get("cod") != 200:
        print("❌ Error:", data.get("message", "Unknown error"))
        return


    weather = data['weather'][0]['description']
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    wind = data['wind']['speed']

    print(f"\n📍 Weather in {city.capitalize()}:")
    print(f"🌡️ Temperature: {temp}°C")
    print(f"🌤️ Condition: {weather.capitalize()}")
    print(f"💧 Humidity: {humidity}%")
    print(f"🍃 Wind Speed: {wind} m/s\n")

api_key = "f6690c61c334bb562de8069839484d70"


while True:
    city_name = input("Enter city name (or type 'exit' to quit): ")
    if city_name.lower() == "exit":
        print("👋 Goodbye!")
        break
    get_weather(city_name, api_key)

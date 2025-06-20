import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = "f6690c61c334bb562de8069839484d70"

def get_weather():
    city = city_entry.get()
    if not city or city == placeholder:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if data.get("cod") != 200:
            messagebox.showerror("Error", f"City not found: {city}")
            return

        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        result_text.set(
            f"📍 {city.title()}\n"
            f"🌡️ {temp}°C\n"
            f"🌤️ {weather.title()}\n"
            f"💧 Humidity: {humidity}%\n"
            f"🍃 Wind: {wind} m/s"
        )

    except requests.RequestException:
        messagebox.showerror("Error", "Could not fetch weather data.")


root = tk.Tk()
root.title("Weather App")
root.geometry("300x300")
root.resizable(False, False)

placeholder = "Enter city"
has_placeholder = True

def clear_placeholder(event):
    global has_placeholder
    if has_placeholder:
        city_entry.delete(0, tk.END)
        city_entry.config(fg="white")
        has_placeholder = False

def restore_placeholder(event):
    global has_placeholder
    if city_entry.get() == "":
        city_entry.insert(0, placeholder)
        city_entry.config(fg="grey")
        has_placeholder = True

city_entry = tk.Entry(root, font=("Arial", 14), fg="grey")
city_entry.insert(0, placeholder)
city_entry.pack(pady=10)


city_entry.bind("<FocusIn>", clear_placeholder)
city_entry.bind("<FocusOut>", restore_placeholder)
city_entry.bind("<Button-1>", clear_placeholder)  
city_entry.bind("<Key>", clear_placeholder)       


tk.Button(root, text="Get Weather", command=get_weather).pack(pady=10)

result_text = tk.StringVar()
tk.Label(root, textvariable=result_text, font=("Arial", 18), justify="center").pack(pady=20)

root.mainloop()

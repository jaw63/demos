import requests
import tkinter as tk

# Set up the OpenWeatherMap API key and endpoint
api_key = [ADD YOUR API KEY HERE]
url = "http://api.openweathermap.org/data/2.5/weather"

# Define a function to retrieve the weather conditions for a given location
def get_weather(city):
    params = {"appid": api_key, "q": city, "units": "metric"}
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print(f"Error: Failed to retrieve weather data for {city}.")
        print(f"Status code: {response.status_code}")
        print(f"Response content: {response.content}")
        return None
    data = response.json()
    try:
        temperature = round((data["main"]["temp"])*(1.80)+32.0,1)
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        weather_description = data["weather"][0]["description"]
        return f"Temperature: {temperature} °F\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s\nWeather Description: {weather_description}"
    except KeyError:
        print(f"Error: Failed to retrieve weather data for {city}.")
        print(f"Response content: {response.content}")
        return None


# Create a GUI window using Tkinter
root = tk.Tk()
root.title("Weather App")

# Define a function to retrieve the weather conditions for the user-specified location
def get_weather_for_location():
    city = city_entry.get()
    weather = get_weather(city)
    weather_label.config(text=weather)

# Create a label for the city input
city_label = tk.Label(root, text="Enter a city:")
city_label.pack()

# Create an entry field for the city input
city_entry = tk.Entry(root)
city_entry.pack()

# Create a button to retrieve the weather conditions for the user-specified location
get_weather_button = tk.Button(root, text="Get Weather", command=get_weather_for_location)
get_weather_button.pack()

# Create a label to display the weather information
weather_label = tk.Label(root, text="")
weather_label.pack()

# Run the GUI main loop
root.mainloop()

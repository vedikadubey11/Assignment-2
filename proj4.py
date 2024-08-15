import requests
import json

def get_weather(location, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return

    weather_data = response.json()
    if "cod" in weather_data and weather_data["cod"] != "404":
        if "main" in weather_data and "temp" in weather_data["main"] and "humidity" in weather_data["main"]:
            main_data = weather_data["main"]
            temperature = main_data["temp"]
            humidity = main_data["humidity"]
            if "weather" in weather_data and len(weather_data["weather"]) > 0 and "description" in weather_data["weather"][0]:
                weather_desc = weather_data["weather"][0]["description"]
                print(f"Weather in {location}:")
                print(f"Temperature: {temperature}°C")
                print(f"Humidity: {humidity}%")
                print(f"Weather: {weather_desc}")
            else:
                print("Error: unable to retrieve weather description")
        else:
            print("Error: unable to retrieve main weather data")
    else:
        print("City Not Found")

def main():
    #print("Welcome to the Weather Fetcher!")
    api_key = "8dcd4936999960e132f25892d5a308ed"
    if not api_key.strip():  # Check for empty or whitespace-only input
        print("Error: API key cannot be empty")
        return
    location = input("Enter a city or location: ")
    if not location.strip():  # Check for empty or whitespace-only input
        print("Error: location cannot be empty")
        return
    get_weather(location, api_key)

if __name__ == "__main__":
    main()

import requests

def get_city_weather(city_name):
    """
    Fetch and display weather information for a given city.
    If the city is invalid, inform the user with a clear error message.
    """
    api_key = "38da8fe81315f7c2fc2a539748f3f28d"
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        if data.get("cod") != 200:
            print("Error: City not found. Please enter a valid city.")
            return

        city = data.get("name", city_name)
        temperature = data.get("main", {}).get("temp", "N/A")
        humidity = data.get("main", {}).get("humidity", "N/A")
        weather_desc = data.get("weather", [{}])[0].get("description", "N/A").capitalize()

        print(f"City: {city}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {weather_desc}")

    except requests.exceptions.RequestException:
        print("Error: City not found. Please enter a valid city.")

if __name__ == "__main__":
    city = input("Enter city name: ").strip()
    get_city_weather(city)

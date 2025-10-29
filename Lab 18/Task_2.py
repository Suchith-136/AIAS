import requests

def display_weather_details(city_name):
    """
    Fetch and display weather details for a specified city using an API.
    Displays formatted weather details with error handling.
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
        weather_data = response.json()

        if weather_data.get("cod") != 200:
            error_message = weather_data.get("message", "Unknown error occurred.")
            print(f"Error: {error_message.capitalize()}")
            return

        name = weather_data.get("name", city_name)
        main = weather_data.get("main", {})
        weather = weather_data.get("weather", [{}])[0]

        temperature = main.get("temp", "N/A")
        feels_like = main.get("feels_like", "N/A")
        humidity = main.get("humidity", "N/A")
        conditions = weather.get("description", "N/A").title()

        print(f"Weather in {name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Feels like: {feels_like}°C")
        print(f"Humidity: {humidity}%")
        print(f"Conditions: {conditions}")

        # Also display raw JSON output
        print("\nWeather details as JSON output:")
        import json
        print(json.dumps(weather_data, indent=4))

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    city = input("Enter city name: ").strip()
    display_weather_details(city)




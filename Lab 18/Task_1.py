import requests

def get_weather(city, api_key):
    # OpenWeatherMap API base URL (current weather endpoint)
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    # Parameters for the API request
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # For temperature in Celsius
    }
    
    # Make API request
    response = requests.get(base_url, params=params)
    
    # Check HTTP status first
    if response.status_code != 200:
        # Try to get JSON error message, otherwise fall back to text
        try:
            err = response.json()
        except ValueError:
            err = response.text
        raise RuntimeError(f"API request failed with status {response.status_code}: {err}")

    # Parse JSON body safely
    try:
        weather_data = response.json()
    except ValueError as e:
        # Response wasn't valid JSON (could be HTML error page)
        raise RuntimeError(f"Failed to parse JSON response: {e}\nResponse text:\n{response.text}")

    return weather_data

# Example usage
if __name__ == "__main__":
    # Your OpenWeatherMap API key
    api_key = input("Enter your OpenWeatherMap API key: ")
    if not api_key:
        print("Error: API key is required. Get one from https://openweathermap.org/api")
        exit(1)
        
    city = input("Enter city name: ")
    if not city:
        print("Error: City name is required")
        exit(1)
        
    try:
        weather = get_weather(city, api_key)
        # Pretty print the weather information
        if 'main' in weather:
            print(f"\nWeather in {city.title()}:")
            print(f"Temperature: {weather['main']['temp']}°C")
            print(f"Feels like: {weather['main']['feels_like']}°C")
            print(f"Humidity: {weather['main']['humidity']}%")
            if 'weather' in weather and weather['weather']:
                print(f"Conditions: {weather['weather'][0]['description'].title()}")
        else:
            print(f"Unexpected API response format: {weather}")
    except Exception as e:
        print(f"Error: {str(e)}")
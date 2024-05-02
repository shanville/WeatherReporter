import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data["main"]["temp"]

def main():
    city = "Tokyo"
    api_key = "0cb1d0452e4232a8819db81766306c86" 
    temp = get_weather(city, api_key)
    print(f"The current temperature in {city} is {temp}°C")

if __name__ == "__main__":
    main()
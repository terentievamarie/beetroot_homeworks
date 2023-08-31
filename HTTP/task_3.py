import requests
import json

def get_weather(city, api_key):
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(url, params = params)
    data = response.json()
    return data

def main():
    api_key = input("Enter your Api Key: ")
    city = input("Enter your city: ")

    weather_data = get_weather(api_key = api_key, city = city)
    if 'main' in weather_data:
        print("It's", weather_data['main']['temp'], f"°C in {city}.", "Feels like ",weather_data['main']['feels_like'], f"°C")
    else:
        print('Weather data retrieval failed.')

    if 'weather' in weather_data:
        print('Weather :', weather_data['weather'][0]['main'])
    else:
        print('Weather data retrieval failed.')

main()
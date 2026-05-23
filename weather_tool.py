import pandas as pd

import requests

city = input("Enter a City: ")

geo_params = {
    'name': city,
    'count': 1,
}

geo_requests = requests.get('https://geocoding-api.open-meteo.com/v1/search', params=geo_params)
geo_data = geo_requests.json()
# print(geo_data)

location = geo_data['results'][0]
lat = location['latitude']
lon = location['longitude']
# print(lat, lon)

weather_params = {
    'latitude': lat,
    'longitude': lon,
    'current_weather': True,
}

weather_response = requests.get('https://api.open-meteo.com/v1/forecast', params=weather_params)
weather_data = weather_response.json()
current = weather_data['current_weather']

weather_conditions = {
    0: 'Clear sky',
    1: 'Mainly clear',
    2: 'Partly cloudy',
    3: 'Overcast',
    45: 'Foggy',
    48: 'Icy fog',
    51: 'Light drizzle',
    61: 'Light rain',
    63: 'Moderate rain',
    65: 'Heavy rain',
    80: 'Rain showers',
    95: 'Thunderstorm',
    99: 'Thunderstorm with hail'
}

code = current['weathercode']
condition = weather_conditions[code]


print(f"Weather in {city}: ")
print(f"Conditions in {city} are: {weather_conditions[code]}")
print(f"Temperature: {current['temperature']} C")
print(f"Wind Speed: {current['windspeed']} Km/h")
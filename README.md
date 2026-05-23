# Weather Tool

A Python CLI tool that fetches live weather data for any city in the world.

## What it does
- Takes a city name as user input
- Converts it to coordinates using the Open-Meteo Geocoding API
- Fetches live weather data using the Open-Meteo Weather API
- Displays current weather conditions (clear sky, rain, thunderstorms, etc.)
- Returns current temperature and wind speed

## Requirements
- Python
- Pandas
- requests

Install dependencies:
pip install pandas requests

## How to run
python weather_tool.py
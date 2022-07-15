import argparse
import json
import sys
from configparser import ConfigParser
from urllib import error, parse, request
from pprint import pp

BASE_WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather"

def _get_api_key():
    config = ConfigParser()
    config.read("secrets.ini")
    return config["openweather"]["api_key"]

def read_user_cli_args():
    parser = argparse.ArgumentParser(
        description="gets weather and temperature information for a city"
    )
    parser.add_argument(
        "city",
        nargs="+",
        type=str,
        help="enter the city name"
    )
    parser.add_argument(
        "-i",
        "--imperial",
        action="store_true",
        help="display the temperature in imperial units",
    )
    return parser.parse_args()

def build_weather_query(city_input, imperial=False):
    api_key = _get_api_key()
    city_name = " ".join(city_input)
    url_encoded_city_name = parse.quote_plus(city_name)
    units = "imperial" if imperial else "metric"
    url = (f"{BASE_WEATHER_API_URL}?q={url_encoded_city_name}"
           f"&units={units}&appid={api_key}")
    return url

def get_weather_data(query_url):
    try:
        response = request.urlopen(query_url)
    except error.HTTPError as http_error:
        if http_error.code == 401:
            sys.exit("Access denied. Check your API Key.")
        elif http_error.code == 404:
            sys.exit("Can't find the weather data for this city.")
        else:
            sys.exit(f"Something went wrong ...{http_error.code}")
    data = response.read()
    try:
        return json.loads(data)
    except json.JSONDecodeError:
        sys.exit("Couldn't read the server response")

if __name__ == '__main__':
    url = build_weather_query(read_user_cli_args().city, read_user_cli_args().imperial)
    weather_data = get_weather_data(url)
    pp(weather_data)

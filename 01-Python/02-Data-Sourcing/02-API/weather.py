# pylint: disable=missing-module-docstring

import sys
#import urllib.parse
import requests

BASE_URI = "https://www.metaweather.com"

def search_city(query):
    '''Look for a given city and disambiguate between several candidates. Return one city (or None)'''
    add_url = "/api/location/search/"
    response = requests.get(
        BASE_URI + add_url,
        params={
            'query': query
        },
    ).json()
    if response ==[]:
        print('City not found')
        return None
    return response[0]

def weather_forecast(woeid):

    url_we = BASE_URI + '/api/location/' + str(woeid)
    consu_w = requests.get(url_we).json()
    return consu_w['consolidated_weather']

def main():
    '''Ask user for a city and display weather forecast'''
    query = input("City?\n> ")
    city = search_city(query)
    if city is not None:

        list = weather_forecast(city['woeid'])

        print(f"Here's the weather in {city['title']}")

        for i in list[:4]:
            print(
                f'{i["applicable_date"]}: {i["weather_state_name"]} {round(i["the_temp"],2)}°C')

if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('\nGoodbye!')
        sys.exit(0)

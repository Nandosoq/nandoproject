# pylint: disable=missing-docstring

import sys
import datetime
import requests
from weather import search_city
BASE_URI = "https://www.metaweather.com"

def daily_forecast(woeid, year, month, day):

    response = requests.get(BASE_URI + '/api/location/' + str(woeid) + '/' + str(year) +
    '/' + str(month) + '/' + str(day)).json()

    return response

def monthly_forecast(woeid, year, month):
    """ return a `list` of forecasts for the whole month """
    pass  # YOUR CODE HERE

def write_csv(woeid, year, month, city, forecasts):
    """ dump all the forecasts to a CSV file in the `data` folder """
    pass  # YOUR CODE HERE

def main():
    if len(sys.argv) > 2:
        city = search_city(sys.argv[1])
        if city:
            woeid = city['woeid']
            year = int(sys.argv[2])
            month = int(sys.argv[3])
            if 1 <= month <= 12:
                forecasts = monthly_forecast(woeid, year, month)
                if not forecasts:
                    print("Sorry, could not fetch any forecast")
                else:
                    write_csv(woeid, year, month, city['title'], forecasts)
            else:
                print("MONTH must be a number between 1 (Jan) and 12 (Dec)")
                sys.exit(1)
    else:
        print("Usage: python history.py CITY YEAR MONTH")
        sys.exit(1)


if __name__ == '__main__':
    main()

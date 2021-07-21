import requests

URL_WE = "https://www.metaweather.com/api/location/search/?query=london"
response = requests.get(URL_WE).json()
city = response[0]

print(f"{city['title']}: {city['woeid']} ({city['latt_long']})")

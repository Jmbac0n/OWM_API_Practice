import requests
import json

key = 'API Key'

url = 'http://api.openweathermap.org/data/2.5/weather?'

location_input = input()

full_url = url + 'q=' + location_input + '&appid=' + key

r = requests.get(full_url)

x = r.json()

y = x['main']

z = y['temp']

celsius = z - 273.15

print("The temperature is: " + "%.2f" % celsius + "C")


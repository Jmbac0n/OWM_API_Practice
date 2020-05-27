import requests
import json

key = 'API key'

url = 'http://api.openweathermap.org/data/2.5/weather?'

print("Please enter a location:")

location_input = input()

print("")

full_url = url + 'q=' + location_input + '&appid=' + key

r = requests.get(full_url)

x = r.json()

def readout():

    celsius_sub = 273.15

    owm_weather = x['weather']
    owm_main = x['main']
    owm_wind = x['wind']

    sky_description = owm_weather[0]
    temp = owm_main['temp']
    fl_temp = owm_main['feels_like']
    wind_spd = owm_wind['speed']

    temp_celsius = temp - celsius_sub
    fl_temp_celsius = fl_temp - celsius_sub
    
    print("Sky status: " + sky_description['main'])
    print("The temperature is: " + "%.2f" % temp_celsius + "C")
    print("The temperature feels like: " + "%.2f" % fl_temp_celsius + "C")
    print("Wind speed is: " + (str(wind_spd)) + "m/s")
    
readout()

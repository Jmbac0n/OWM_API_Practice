import sys
import datetime
import requests
import json

def main():

    #Set up for API call + Date/Time
    key = 'OWM API Key'

    url = 'http://api.openweathermap.org/data/2.5/weather?'
    
    today = datetime.datetime.now()

    print("Please enter a location:")

    location_input = input()

    print("")

    full_url = url + 'q=' + location_input + '&appid=' + key

    r = requests.get(full_url)

    x = r.json()

    #Calls for API information
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

    #Outputs the results into a file
    orig_stdout = sys.stdout
    f = open('owm_history', 'a')
    sys.stdout = f

    print("Location: " + location_input)
    print("")
    print("Sky status: " + sky_description['main'])
    print("The temperature is: " + "%.2f" % temp_celsius + "C")
    print("The temperature feels like: " + "%.2f" % fl_temp_celsius + "C")
    print("Wind speed is: " + (str(wind_spd)) + "m/s")
    print("")
    print(today)
    print("")

    sys.stdout = orig_stdout
    f.close()

    #Outputs the results in the console
    print("Location: " + location_input)
    print("")
    print("Sky status: " + sky_description['main'])
    print("The temperature is: " + "%.2f" % temp_celsius + "C")
    print("The temperature feels like: " + "%.2f" % fl_temp_celsius + "C")
    print("Wind speed is: " + (str(wind_spd)) + "m/s")
    print("")
    print(today)
    print("")
    

    #Asks user if they want to search a new location or quit
    def reset():
        print("Search new location: (y/n)")
        reset_input = input()
        if reset_input == ("y"):
            print("")
            main()
        elif reset_input == ("n"):
            print("")
            quit()
        else:
            print("Invalid input")
            reset() #Keeps asking until valid input

    reset()
main()

# TODO
# Refactor

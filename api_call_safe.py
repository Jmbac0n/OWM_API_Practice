import sys, datetime, requests, json

def main():

    #Set up for API call + Date/Time
    key = 'API Key'

    url = 'http://api.openweathermap.org/data/2.5/weather?'
    
    today = datetime.datetime.now()

    print("Please enter a location:")

    # Invalid input currently creates error and crash
    location_input = input()

    print("")

    full_url = url + 'q=' + location_input + '&appid=' + key

    r = requests.get(full_url)

    x = r.json()

    cod_check = x['cod']
    bad_request = "404"

    #Converts temperature from kelvin to celsius as a return function

    def temp_conversion(int):

        celsius_sub = 273.15
        celsius_temp = int - celsius_sub
        return celsius_temp

    #Outputs the results in the console
    
    def readout():

        #Calls specified API information
    
        owm_weather = x['weather']
        owm_main = x['main']
        owm_wind = x['wind']
    
        sky_description = owm_weather[0]
        temp = owm_main['temp']
        fl_temp = owm_main['feels_like']
        wind_spd = owm_wind['speed']

        #Prints it out

        print("Location: " + location_input)
        print("")
        print("Sky status: " + sky_description['main'])
        print("The temperature is: " + "%.2f" % temp_conversion(temp) + "C")
        print("The temperature feels like: " + "%.2f" % temp_conversion(fl_temp) + "C")
        print("Wind speed is: " + (str(wind_spd)) + "m/s")
        print("")
        print(today)
        print(cod_check)
        print("")

    #Saves the result into a file
    def file_save():
        orig_stdout = sys.stdout
        f = open('owm_history', 'a')
        sys.stdout = f

        readout()

        sys.stdout = orig_stdout
        f.close()
    
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
            print("Invalid response")
            reset() #Keeps asking until valid input

    #Checks cod variable for 404 bad request - Returned in json if API can't find location
    if cod_check == bad_request:
        print("Error 404: Bad request please enter another location")
        print("")
        main()
    else:
    #Print readout into console + saves readout to text file + ask user to reset function
        readout()
        file_save()
        reset()
main()

# TODO

# Refactor TODO
# Tidy up error checking code

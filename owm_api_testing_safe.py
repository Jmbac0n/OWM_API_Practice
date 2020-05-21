import pyowm
owm = pyowm.OWM('API key goes here')
observation = owm.weather_at_place('London, UK')
weather = observation.get_weather()
print(weather)

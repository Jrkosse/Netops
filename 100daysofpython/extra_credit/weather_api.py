# Day 13 was a lot on debugging that I've done many times. Concepts are familiar. Writing something I don't know to practice. 
# Chapter 14 of "Automate the Boring Stuff"
#
#
# Weather App
# Prints the weather for a location from the command line

import json, requests, sys

# Get location from Arg
# sys.argv[0] will be the script name. [1] will be the location
if len(sys.argv) < 2:
    print('Usage: python script.py location')
    sys.exit()

# We join the args to avoid spaces indicating that there are more args being passed than intended.
location = ' '.join(sys.argv[1:])
key = "Get Your own!!!"
url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={key}"

# Pass the URL into requests.get and assign that to response
response = requests.get(url)

# Check for issues with the response
response.raise_for_status()

# Load json data into a variable
weatherData = json.loads(response.text)

# Select the 'main' section of the API response and calculate Fahrenheit from Kelvin
temp = weatherData['main']
current_temp_kelvin = temp['temp']
current_temp_fahrenheit = round((current_temp_kelvin - 273.15) * 9/5 + 32,1)

# Select the 'weather' section of the API response
weather = weatherData['weather']
current_weather = weather[0]['description']

# Print output
print(f"Current weather in {location} is: {current_temp_fahrenheit} and is {current_weather}")

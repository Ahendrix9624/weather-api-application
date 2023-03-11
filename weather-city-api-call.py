"""
USAGE - This code retrieves weather data for a user-specified city using the OpenWeatherMap API. 
        The API key is obtained from an environmental variable named WEATHER_API_KEY. The user is 
        prompted to enter a city name, and the code constructs a URL using the API key and 
        city name. A GET request is sent to the API, and the response is parsed as JSON. 
        The script then extracts the weather description and temperature data from the 
        JSON response, and converts the temperature from Kelvin to Celsius and Fahrenheit. 
        The results are printed to the console. If an error occurs, the script prints an error message.

AUTHOR - https://github.com/Ahendrix9624/
"""

import requests
import os

API_KEY = os.environ.get("WEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?q="

city = input("Enter a city name: ")
requests_url = f"{BASE_URL}{city}&appid={API_KEY}"
response = requests.get(requests_url)

# This can be used to test the api call or uncomment this to see how the info below gets pulled from the API
# data = response.json()
# print(data)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description'] 
    celsius_temperature = round(data["main"]["temp"] - 273.15, 2)       #Kelvin to celsius conversion, round two digits
    fahrenheit_temperature = round((data["main"]["temp"] - 273.15) * 9/5 + 32, 2)   #Kelvin to fahrenheit conversion, round two digits
    
    
    print("Weather:", weather)
    print("Temperature:", celsius_temperature, "celsius")
    print("Temperature:", fahrenheit_temperature, "fahrenheit")
else:
    print("An error occurred.")

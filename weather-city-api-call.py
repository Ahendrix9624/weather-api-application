# Free weather API https://openweathermap.org/

# import requests HTTP Library module
import requests

API_KEY = "9afd1eb66741444d53f93555e9008535"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?q="

city = input("Enter a city name: ")
requests_url = f"{BASE_URL}{city}&appid={API_KEY}"
response = requests.get(requests_url)

# This can be used to test the api call
data = response.json()
print(data)

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
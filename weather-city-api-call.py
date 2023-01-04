#!/usr/bin/env python3
#
#  [Program]
#
#  Weather City Api Call
#
#  [Author]
#
#  Drew, https://github.com/Ahendrix9624/
#
#  [License]
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
#  See 'LICENSE' for more information.

# import requests HTTP Library module
import requests

API_KEY = "9afd1eb66741444d53f93555e9008535"
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
import requests
import json_api
from datetime import datetime
WhetherAPI_Key = '68d486e7a27b08b2701d099f742489a5'
#Input from the user for loaction
location = input('Enter the name of Your City: ')
Full_WeatherAPI_Link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + WhetherAPI_Key
WeatherAPI_Link = requests.get(Full_WeatherAPI_Link)
WeatherAPI_Data = WeatherAPI_Link.json()
#Longitude of Your given Location
longitude = WeatherAPI_Data['coord']['lon']
#Latitude of Your given Location
latitude = WeatherAPI_Data['coord']['lat']
#Tempature of Your given Location
temperature = ((WeatherAPI_Data['main']['temp']) - 273.15)
#Weather Description of Your given Location
desrp = WeatherAPI_Data['weather'][0]['description']
#Humidity of Your given Location
humidity = WeatherAPI_Data['main']['humidity']
#Pressure of Your given Location
pressure = WeatherAPI_Data['main']['pressure']
#Wind Direction at Your given Location
WindSpd = WeatherAPI_Data['wind']['speed']
today = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
#Displaying All this Information
print("Your City      : ",location)
print("Longitude      : ",longitude)
print("Latitude       : ",latitude)
print("Temperature    : ",temperature, " C")
print("Description    : ",desrp)
print("Humidity       : ",humidity," %")
print("Pressure       : ",pressure," hPa")
print("Wind Speed     : ",WindSpd, " m/s")
#Recording the Information in txt format
#The file will be downloaded in PC
with open('Weather_info','wb') as f:
    f.write(WeatherAPI_Link.content)
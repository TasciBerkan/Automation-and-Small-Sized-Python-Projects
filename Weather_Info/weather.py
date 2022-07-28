import requests
import api_key

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url=f"{BASE_URL}?appid={api_key.API_KEY}&q={city}"
response=requests.get(request_url)

if response.status_code==200:
    data = response.json()
    #print(data)
    weather=data['weather'][0]['description']
    temperature = round(data["main"]["temp"]-272)
    print("Weather: ", weather)
    print("Temperature: ", temperature, "celcius")
else:
    print("An error occurres")
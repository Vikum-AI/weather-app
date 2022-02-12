import requests

API_KEY = 'ccf7536c21a37d8dd1ccedce3ad49d4b'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

city = input("Enter city name: ")
request_url = f'{BASE_URL}?appid={API_KEY}&q={city}'
response = requests.get(request_url)

if response.status_code == 200: 
	data = response.json() 
	weather = data['weather'][0]['description']
	temperature = round(data["main"]["temp"] - 273.15, 2) 
	
	print("Weather:", weather) 
	print("Temperature:", temperature, "°C")

else: 
	print("Error fetching data") 

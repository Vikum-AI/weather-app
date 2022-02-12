import requests

API_KEY = 'ccf7536c21a37d8dd1ccedce3ad49d4b'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

city = input("Enter city name: ")
request_url = f'{BASE_URL}?appid={API_KEY}&q={city}'
response = requests.get(request_url)
data = response.json() 
print(data)  



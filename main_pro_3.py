import requests

from pprint import pprint


API_Key='fed0338161f098078481eec10f2e5e92'
city=input('Enter a City:')
url=f'http://api.openweathermap.org/data/2.5/forecast?appid={API_Key}&q={city}'
weather_data=requests.get(url).json()
pprint(weather_data)
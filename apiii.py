import requests

url = 'https://lightpollutionmap.app/?lat=40.780734&lng=-73.967171&zoom=14'
response = requests.get(url)
print(response)

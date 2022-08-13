import requests

city = input("Enter you desired country: ")
print(city)

print('Weather Report for:'+ city)

url = 'https://wttr.in/{}'.format (city)
resource = requests.get(url)

print(resource.text)


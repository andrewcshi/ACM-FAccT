import requests

url = 'https://facctconference.org/2020/acceptedpapers'
response = requests.get(url)
with open('facctpapers20.html', 'w') as file:
    file.write(response.text)
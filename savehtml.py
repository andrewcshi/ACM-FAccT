import requests

url = 'https://facctconference.org/2022/acceptedpapers'
response = requests.get(url)
with open('facctpapers22.html', 'w') as file:
    file.write(response.text)
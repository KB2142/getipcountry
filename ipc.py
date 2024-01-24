import requests

response = requests.get("https://api.country.is/")
print(response.text.replace(',', '\n').replace('"', '').replace('{', '').replace('}', ''))

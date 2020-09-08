import requests

payload = requests.get("https://dog.ceo/api/breeds/image/random")
if payload.status_code == 200:
    
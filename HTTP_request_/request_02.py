import requests
url = "https://icanhazdadjoke.com/"

response = requests.get(url, headers={"Accept": "application/json"})
# print(response.text)
data = response.json()
print(data["joke"])
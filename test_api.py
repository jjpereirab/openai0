import requests

# url = "https://randomuser.me/api/"
book = "classical electrodynamics"

url = f"https://openlibrary.org/search.json?q={book}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
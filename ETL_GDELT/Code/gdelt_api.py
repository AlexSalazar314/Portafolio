import requests

url = "https://api.gdeltproject.org/api/v2/doc/doc"

params = {
    "query": '"climate change"',
    "mode": "artlist",
    "maxrecords": 10,
    "timespan": "1day",
    "format": "json"
}

response = requests.get(url, params=params)

print("Status:", response.status_code)

if response.status_code == 200:
    data = response.json()

    print("Número de artículos:", len(data["articles"]))

    for article in data["articles"]:
        print(article)

elif response.status_code == 429:
    print("GDELT está limitando las solicitudes.")
    print(response.text)

else:
    print("Error:", response.status_code)
    print(response.text)
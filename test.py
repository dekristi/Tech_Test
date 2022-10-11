import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/albums"
response = requests.get(url)
print(response.status_code)

df = pd.read_json(url)  # so includes parsing and request to the server
print(df.head(10))
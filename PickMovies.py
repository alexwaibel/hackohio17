import requests
import json

apikey = "e7552b83b0a1458bf2caadfe42e02de5"
main_api = "https://api.themoviedb.org"
url = main_api + "/3/genre/tv/list?language=en-US&api_key=" + apikey
response = requests.get(url)
genres = response.json()
print(genres)
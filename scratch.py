import os
import json, urllib.request 

url = "https://api.quotable.io/random?maxLength=300"

response = urllib.request.urlopen(url)
data = response.read()
dict = json.loads(data)
quote = dict['content']

print(quote)
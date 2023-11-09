import requests

api_key = 'ec51019a-3d2a-40d1-8716-e3f6252e643b'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'
res = requests.get(url)
definition = res.json()
print(definition)

for definitions in definition:
    print(definition)
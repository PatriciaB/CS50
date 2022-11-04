import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

#print(response.json())      #para mostrar na tela
#print(json.dumps(response.json(), indent=2))      #formatado

o = response.json()  #arquivar a resposta

for result in o["results"]:
    print(result["trackName"])
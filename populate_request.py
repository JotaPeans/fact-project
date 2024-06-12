import requests

url = 'http://127.0.0.1:8000/app/populate'

# Fazendo a requisição GET
resposta = requests.get(url)

print(resposta.json())
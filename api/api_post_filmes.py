import requests
import json

IP = "localhost" # Substitua pelo IP do servidor
PORT = "3000" # Porta utilizada

# Dados do novo filme a ser adicionado
f = open("/Matheus/Documents/UFF/UFF - 7 período/sistemas_distribuidos/t3_2/files/novo_filme.json", 'r')
dados = json.load(f)
f.close()

novo_filme = {
    "title": dados["title"],
    "description": dados["description"],
    "release_year": dados["release_year"],
    "language_id": dados["language_id"],
    "rental_duration": dados["rental_duration"],
    "rental_rate": dados["rental_rate"],
    "length": dados["length"],
    "replacement_cost": dados["replacement_cost"],
    "rating": dados["rating"],
    "special_features": dados["special_features"],
}

# Fazer uma solicitação POST para adicionar um novo filme
url_adicionar_filme = f"http://{IP}:{PORT}/filmes"
response_adicionar_filme = requests.post(url_adicionar_filme, json=novo_filme)

if response_adicionar_filme.status_code == 200:
    resultado_adicionar_filme = response_adicionar_filme.json()
    print("Resultado da Adição de Filme:")
    print(resultado_adicionar_filme)
else:
    print(f"Erro ao adicionar Filme: {response_adicionar_filme.status_code}")

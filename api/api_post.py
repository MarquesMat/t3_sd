import base64
import requests
import json
import sys

IP = "localhost"  
PORT = "3000"  
FILES_PATH = "C:/Users/davi2/OneDrive/Documentos/sd3/t3_sd/files"

usuario = sys.argv[1]
senha = sys.argv[2]

# Criar a string de autenticação para o Basic Auth
credenciais = f'{usuario}:{senha}'
autenticacao = base64.b64encode(credenciais.encode('utf-8')).decode('utf-8')
headers = {'Authorization': f'Basic {autenticacao}'}

if sys.argv[3] == "filme":
    # Dados do novo filme a ser adicionado
    with open(FILES_PATH + "/novo_filme.json", 'r') as f:
        dados = json.load(f)

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
    url_adicionar = f"http://{IP}:{PORT}/filmes"
    response_adicionar = requests.post(url_adicionar, json=novo_filme, headers=headers)

    if response_adicionar.status_code == 200:
        resultado_adicionar = response_adicionar.json()
        print("Resultado da Adição de Filme:")
        print(resultado_adicionar)
    else:
        print(f"Erro ao adicionar Filme: {response_adicionar.status_code}")
elif sys.argv[3] == "ator":
    # Dados do novo filme a ser adicionado
    with open(FILES_PATH + "/novo_ator.json", 'r') as f:
        dados = json.load(f)

    novo_ator = {
        "first_name": dados["first_name"],
        "last_name": dados["last_name"],
    }

    # Fazer uma solicitação POST para adicionar um novo filme
    url_adicionar = f"http://{IP}:{PORT}/atores"
    response_adicionar = requests.post(url_adicionar, json=novo_ator, headers=headers)

    if response_adicionar.status_code == 200:
        resultado_adicionar = response_adicionar.json()
        print("Resultado da Adição de Ator:")
        print(resultado_adicionar)
    else:
        print(f"Erro ao adicionar Ator: {response_adicionar.status_code}")
elif sys.argv[3] == "categoria":
    # Dados do novo filme a ser adicionado
    with open(FILES_PATH + "/nova_categoria.json", 'r') as f:
        dados = json.load(f)

    nova_categoria = {
        "name": dados["name"],
    }

    # Fazer uma solicitação POST para adicionar um novo filme
    url_adicionar = f"http://{IP}:{PORT}/categorias"
    response_adicionar = requests.post(url_adicionar, json=nova_categoria, headers=headers)

    if response_adicionar.status_code == 200:
        resultado_adicionar = response_adicionar.json()
        print("Resultado da Adição de Categoria:")
        print(resultado_adicionar)
    else:
        print(f"Erro ao adicionar Categoria: {response_adicionar.status_code}")
else:
    print("Erro de endpoints")

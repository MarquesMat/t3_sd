import requests
import json
import sys

IP = "localhost" # Substitua pelo IP do servidor
PORT = "3000" # Porta utilizada
FILES_PATH = "C:/Users/davi2/OneDrive/Documentos/sd3/t3_sd/files"

if sys.argv[1] == "filme":
    # Dados do novo filme a ser adicionado
    f = open(FILES_PATH + "/novo_filme.json", 'r')
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
    url_adicionar = f"http://{IP}:{PORT}/filmes"
    response_adicionar = requests.post(url_adicionar, json=novo_filme)

    if response_adicionar.status_code == 200:
        resultado_adicionar = response_adicionar.json()
        print("Resultado da Adição de Filme:")
        print(resultado_adicionar)
    else:
        print(f"Erro ao adicionar Filme: {response_adicionar.status_code}")
elif sys.argv[1] == "ator":
    # Dados do novo filme a ser adicionado
    f = open(FILES_PATH +"/novo_ator.json", 'r')
    dados = json.load(f)
    f.close()

    novo_ator = {
        "first_name": dados["first_name"],
        "last_name": dados["last_name"],
    }

    # Fazer uma solicitação POST para adicionar um novo filme
    url_adicionar = f"http://{IP}:{PORT}/atores"
    response_adicionar = requests.post(url_adicionar, json=novo_ator)

    if response_adicionar.status_code == 200:
        resultado_adicionar = response_adicionar.json()
        print("Resultado da Adição de Ator:")
        print(resultado_adicionar)
    else:
        print(f"Erro ao adicionar Ator: {response_adicionar.status_code}")
elif sys.argv[1] == "categoria":
    # Dados do novo filme a ser adicionado
    f = open(FILES_PATH + "/nova_categoria.json", 'r')
    dados = json.load(f)
    f.close()

    nova_categoria = {
        "name": dados["name"],
    }

    # Fazer uma solicitação POST para adicionar um novo filme
    url_adicionar = f"http://{IP}:{PORT}/categorias"
    response_adicionar = requests.post(url_adicionar, json=nova_categoria)

    if response_adicionar.status_code == 200:
        resultado_adicionar = response_adicionar.json()
        print("Resultado da Adição de Categoria:")
        print(resultado_adicionar)
    else:
        print(f"Erro ao adicionar Categoria: {response_adicionar.status_code}")
else:
    print("Erro de endpoints")

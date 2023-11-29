# import requests
# import json
# import sys

# IP = "localhost" # Substitua pelo IP do servidor
# PORT = "3000" # Porta utilizada

# FILES_PATH = "C:/Users/davi2/OneDrive/Documentos/sd3/t3_sd/files"

# if sys.argv[1] == "filme":
#     # Carrega os dados atualizados do filme de um arquivo JSON
#     with open(FILES_PATH + "/atualizar_filme.json", 'r') as f:
#         dados = json.load(f)

#     # Envia uma solicitação PUT para atualizar o filme
#     url_atualizar = f"http://{IP}:{PORT}/filmes/{dados['id']}"
#     response_atualizar = requests.put(url_atualizar, json=dados)

#     if response_atualizar.status_code == 200:
#         resultado_atualizar = response_atualizar.json()
#         print("Resultado da Atualização de Filme:")
#         print(resultado_atualizar)
#     else:
#         print(f"Erro ao atualizar Filme: {response_atualizar.status_code}")
# elif sys.argv[1] == "ator":
#     # Carrega os dados atualizados do ator de um arquivo JSON
#     with open(FILES_PATH + "/atualizar_ator.json", 'r') as f:
#         dados = json.load(f)

#     # Envia uma solicitação PUT para atualizar o ator
#     url_atualizar = f"http://{IP}:{PORT}/atores/{dados['id']}"
#     response_atualizar = requests.put(url_atualizar, json=dados)

#     if response_atualizar.status_code == 200:
#         resultado_atualizar = response_atualizar.json()
#         print("Resultado da Atualização de Ator:")
#         print(resultado_atualizar)
#     else:
#         print(f"Erro ao atualizar Ator: {response_atualizar.status_code}")
# elif sys.argv[1] == "categoria":
#     # Carrega os dados atualizados da categoria de um arquivo JSON
#     with open(FILES_PATH + "/atualizar_categoria.json", 'r') as f:
#         dados = json.load(f)

#     # Envia uma solicitação PUT para atualizar a categoria
#     url_atualizar = f"http://{IP}:{PORT}/categorias/{dados['id']}"
#     response_atualizar = requests.put(url_atualizar, json=dados)

#     if response_atualizar.status_code == 200:
#         resultado_atualizar = response_atualizar.json()
#         print("Resultado da Atualização de Categoria:")
#         print(resultado_atualizar)
#     else:
#         print(f"Erro ao atualizar Categoria: {response_atualizar.status_code}")
# else:
#     print("Erro de endpoints")

# import requests
# import json
# import sys

# IP = "localhost"  # Substitua pelo IP do servidor
# PORT = "3000"  # Porta utilizada
# TABLE = sys.argv[1]  # Fixando a tabela como "filmes" para esta operação
# ID = sys.argv[2]  # ID do filme a ser atualizado (passado como argumento)
# FILES_PATH = "C:/Users/davi2/OneDrive/Documentos/sd3/t3_sd/files"

# # Carregar os dados de atualização do arquivo JSON
# with open(FILES_PATH + "/filmes.json", "r") as json_file:
#     dados = json.load(json_file)

# # Construir a URL para a tabela e o ID especificado
# url_table_id = f"http://{IP}:{PORT}/{TABLE}"

# # Imprimir a URL para verificar
# print(f"URL: {url_table_id}")

# # Fazer uma solicitação PUT para atualizar um filme
# response_table = requests.put(url_table_id, json=dados)

# if response_table.status_code == 200:
#     resultado_atualizar = response_table.json()
#     print(f"Resultado da Atualização de {TABLE}:")
#     print(resultado_atualizar)
# else:
#     print(f"Erro ao atualizar {TABLE}: {response_table.status_code}")


# import requests
# import json
# import sys

# IP = "localhost"  # Substitua pelo IP do servidor
# PORT = "3000"  # Porta utilizada
# TABLE = "filmes"  # Fixando a tabela como "filmes" para esta operação
# FILES_PATH = "C:/Users/davi2/OneDrive/Documentos/sd3/t3_sd/files"
# ID = sys.argv[1]  # ID do filme a ser atualizado (passado como argumento)


# # Carregar os dados do arquivo filmes.json
# with open(FILES_PATH + "/filmes.json", "r") as json_file:
#     filmes = json.load(json_file)

# # Encontrar o filme com o ID desejado
# filme_atualizar = next((filme for filme in filmes if filme["film_id"] == int(ID)), None)

# # Verificar se o filme foi encontrado
# if filme_atualizar is None:
#     print(f"Erro: Filme com ID {ID} não encontrado.")
#     sys.exit(1)

# # Imprimir os dados do filme antes da atualização
# print(f"Dados do Filme Antes da Atualização:")
# print(json.dumps(filme_atualizar, indent=2))

# # Realizar as atualizações desejadas nos dados do filme
# # Por exemplo, você pode modificar o título do filme
# filme_atualizar["title"] = "Novo Título do Filme"

# # Construir a URL para a tabela e o ID especificado
# url_table_id = f"http://{IP}:{PORT}/{TABLE}/{ID}"

# # Imprimir a URL para verificar
# print(f"URL: {url_table_id}")

# # Fazer uma solicitação PUT para atualizar o filme
# response_table = requests.put(url_table_id, json=filme_atualizar)

# if response_table.status_code == 200:
#     resultado_atualizar = response_table.json()
#     print(f"Resultado da Atualização de {TABLE}:")
#     print(resultado_atualizar)
# else:
#     print(f"Erro ao atualizar {TABLE}: {response_table.status_code}")


import requests
import json
import sys

def load_data(file_path):
    with open(file_path, "r") as json_file:
        return json.load(json_file)

def find_item_by_id(items, item_id):
    return next((item for item in items if item["film_id"] == int(item_id)), None)

def print_item_data(item, message="Dados do Item:"):
    print(message)
    print(json.dumps(item, indent=2))

def update_item_data(item, field, value):
    item[field] = value

def build_url(ip, port, table, item_id):
    return f"http://{ip}:{port}/{table}/{item_id}"

def make_put_request(url, data):
    return requests.put(url, json=data)

def main():
    ip = "localhost"  # Substitua pelo IP do servidor
    port = "3000"  # Porta utilizada
    table = "filmes"  # Fixando a tabela como "filmes" para esta operação
    files_path = "C:/Users/davi2/OneDrive/Documentos/sd3/t3_sd/files"
    item_id = sys.argv[1]  # ID do filme a ser atualizado (passado como argumento)
    update_field = sys.argv[2]  # Campo a ser atualizado
    update_value = sys.argv[3]  # Valor a ser atribuído ao campo

    # Carregar os dados do arquivo filmes.json
    filmes = load_data(files_path + "/filmes.json")

    # Encontrar o filme com o ID desejado
    filme_atualizar = find_item_by_id(filmes, item_id)

    # Verificar se o filme foi encontrado
    if filme_atualizar is None:
        print(f"Erro: Filme com ID {item_id} não encontrado.")
        sys.exit(1)

    # Imprimir os dados do filme antes da atualização
    # print_item_data(filme_atualizar, "Dados do Filme Antes da Atualização:")

    # Realizar as atualizações desejadas nos dados do filme
    update_item_data(filme_atualizar, update_field, update_value)

    # Construir a URL para a tabela e o ID especificado
    url_table_id = build_url(ip, port, table, item_id)

    # Imprimir a URL para verificar
    print(f"URL: {url_table_id}")

    # Fazer uma solicitação PUT para atualizar o filme
    response_table = make_put_request(url_table_id, filme_atualizar)

    if response_table.status_code == 200:
        resultado_atualizar = response_table.json()
        print(f"Resultado da Atualização de {table}:")
        print(resultado_atualizar)
    else:
        print(f"Erro ao atualizar {table}: {response_table.status_code}")

if __name__ == "__main__":
    main()

import requests
import json
import sys

IP = "localhost" # Substitua pelo IP do servidor
PORT = "3000" # Porta utilizada
TABLE = sys.argv[1] # Qual tabela será consultada
# atores, filmes, categorias

if len(sys.argv) > 2: # Buscar uma instância epecífica na tabela
    ID = sys.argv[2] # Qual ID buscar
    url_table = f"http://{IP}:{PORT}/{TABLE}/{ID}"
    path_file = f"/Matheus/Documents/UFF/UFF - 7 período/sistemas_distribuidos/t3_2/files/{TABLE}_{ID}.json"
else: # Buscar todas as informações da tabela
    url_table = f"http://{IP}:{PORT}/{TABLE}"
    path_file = f"/Matheus/Documents/UFF/UFF - 7 período/sistemas_distribuidos/t3_2/files/{TABLE}.json"

response_table = requests.get(url_table)

if response_table.status_code == 200:
        dados = response_table.json()

        # Salvar os dados em um arquivo JSON
        with open(path_file, "w") as json_file:
            json.dump(dados, json_file, indent=2)
            print(f"Dados de {TABLE} salvos em novo arquivo!")

else:
    print(f"Erro na solicitação de {TABLE}: {response_table.status_code}")

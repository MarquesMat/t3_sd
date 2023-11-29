import requests
import json
import sys

IP = "localhost" # Substitua pelo IP do servidor
PORT = "3000" # Porta utilizada
TABLE = sys.argv[1] # Qual tabela será consultada
# atores, filmes, categorias

# Fazer uma solicitação GET para obter dados da tabela atores
url_table = f"http://{IP}:{PORT}/{TABLE}"
response_table = requests.get(url_table)

if response_table.status_code == 200:
    data_atores = response_table.json()

    # Imprimir o resultado no terminal
    #print("Dados de Atores:")
    #print(data_atores)

    # Salvar os dados em um arquivo JSON
    with open(f"C:/Users/davi2/OneDrive/Documentos/sd3/t3_sd/files/{TABLE}.json", "w") as json_file:
        json.dump(data_atores, json_file, indent=2)
        print(f"Dados de {TABLE} salvos em {TABLE}.json")

else:
    print(f"Erro na solicitação de {TABLE}: {response_table.status_code}")

import json
import requests
import sys
import base64

def make_delete_request(url, auth):
    headers = {"Authorization": "Basic " + auth}
    response = requests.delete(url, headers=headers)
    return response

def get_credentials():
    f = open("credentials.json", 'r')
    dados = json.load(f)
    f.close()
    username = dados["user"]
    password = dados["password"]
    credentials = base64.b64encode(f"{username}:{password}".encode()).decode("utf-8")
    return credentials

def main():
    ip = "localhost" # Substitua pelo IP do servidor
    port = "3000" # Porta utilizada
    table = sys.argv[1] # Qual tabela será modificada
    id = sys.argv[2] # Qual instância será deletada
    # atores, filmes, categorias

    # Fazer uma solicitação DELETE para retirar uma instância
    url_table_id = f"http://{ip}:{port}/{table}/{id}"

    auth_credentials = get_credentials()
    response_table = make_delete_request(url_table_id, auth_credentials)

    print(url_table_id)

    if response_table.status_code == 200:
        resultado_excluir_filme = response_table.json()
        print(resultado_excluir_filme)
    else:
        print(f"Erro ao excluir {table}: {response_table.status_code}")

if __name__ == "__main__":
    main()

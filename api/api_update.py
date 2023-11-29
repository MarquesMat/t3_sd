import requests
import json
import sys
import base64

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

def make_put_request(url, data, auth):
    headers = {"Authorization": "Basic " + auth}
    return requests.put(url, json=data, headers=headers)

def get_credentials():
    username = sys.argv[1]
    password = sys.argv[2]
    credentials = base64.b64encode(f"{username}:{password}".encode()).decode("utf-8")
    return credentials

def main():
    ip = "localhost"
    port = "3000"
    table = "filmes"
    files_path = "C:/Users/davi2/OneDrive/Documentos/sd3/t3_sd/files"
    item_id = sys.argv[3]
    update_field = sys.argv[4]
    update_value = sys.argv[5]

    filmes = load_data(files_path + "/filmes.json")
    filme_atualizar = find_item_by_id(filmes, item_id)

    if filme_atualizar is None:
        print(f"Erro: Filme com ID {item_id} não encontrado.")
        sys.exit(1)

    update_item_data(filme_atualizar, update_field, update_value)
    url_table_id = build_url(ip, port, table, item_id)

    print(f"URL: {url_table_id}")

    auth_credentials = get_credentials()
    response_table = make_put_request(url_table_id, filme_atualizar, auth_credentials)

    if response_table.status_code == 200:
        resultado_atualizar = response_table.json()
        print(f"Resultado da Atualização de {table}:")
        print(resultado_atualizar)
    else:
        print(f"Erro ao atualizar {table}: {response_table.status_code}")

if __name__ == "__main__":
    main()

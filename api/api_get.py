import requests
import json
import sys
import base64

def make_get_request(url, auth):
    headers = {"Authorization": "Basic " + auth}
    response = requests.get(url, headers=headers)
    return response

def get_credentials():
    username = sys.argv[1]
    password = sys.argv[2]
    credentials = base64.b64encode(f"{username}:{password}".encode()).decode("utf-8")
    return credentials

def main():
    ip = "localhost"
    port = "3000"
    table = sys.argv[3]

    if len(sys.argv) > 3:
        item_id = sys.argv[4]
        url_table = f"http://{ip}:{port}/{table}/{item_id}"
        file_path = f"C:/Users/davi2/OneDrive/Documentos/sd3/t3_sd/files/{table}_{item_id}.json"
    else:
        url_table = f"http://{ip}:{port}/{table}"
        file_path = f"C:/Users/davi2/OneDrive/Documentos/sd3/t3_sd/files/{table}.json"

    auth_credentials = get_credentials()
    response_table = make_get_request(url_table, auth_credentials)

    if response_table.status_code == 200:
        data = response_table.json()

        # Salvar os dados em um arquivo JSON
        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=2)
            print(f"Dados de {table} salvos em novo arquivo!")
    else:
        print(f"Erro na solicitação de {table}: {response_table.status_code}")

if __name__ == "__main__":
    main()

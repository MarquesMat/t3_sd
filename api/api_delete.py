import requests
import sys
import base64

def make_delete_request(url, auth):
    headers = {"Authorization": "Basic " + auth}
    response = requests.delete(url, headers=headers)
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
    item_id = sys.argv[4]

    # Fazer uma solicitação DELETE para retirar uma instância
    url_table_id = f"http://{ip}:{port}/{table}/{item_id}"

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

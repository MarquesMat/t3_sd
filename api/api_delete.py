import requests
import sys

IP = "localhost" # Substitua pelo IP do servidor
PORT = "3000" # Porta utilizada
TABLE = sys.argv[1] # Qual tabela será modificada
ID = sys.argv[2] # Qual instância será deletada
# atores, filmes, categorias

# Fazer uma solicitação DELETE para retirar uma instância
url_table_id = f"http://{IP}:{PORT}/{TABLE}/{ID}"
response_table = requests.delete(url_table_id)
print(url_table_id)

if response_table.status_code == 200:
    resultado_excluir_filme = response_table.json()
    print(resultado_excluir_filme)
else:
    print(f"Erro ao excluir Filme: {response_table.status_code}")

import requests
from app.config import API_URL

# Função para extrair dados da api
def get_api_data():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Lança um erro se a resposta não for 200
        content = response.json()
        data = content["data"]
        return data
        
    except requests.RequestException as e:
        print(f"Erro ao requisitar os dados da API: {e}")
        return None
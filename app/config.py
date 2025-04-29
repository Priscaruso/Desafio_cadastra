import os
from dotenv import load_dotenv

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# URL da API usada na aplicação
API_URL = os.getenv("API_URL")
from app.ingestion import load_data

# Executa o ETL
if __name__ == "__main__":
    print("Iniciando a coleta dos dados...")
    load_data()
    print("Carregamento finalizado!")
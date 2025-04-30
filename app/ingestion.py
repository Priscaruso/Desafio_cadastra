from app.database import SessionLocal
from app.models import Cryptocurrency, MarketData
from app.api_client import get_api_data

# Função que coleta os dados da API, transforma de acordo com o modelo e carrega os dados no banco
def load_data():
    db = SessionLocal()
    data = get_api_data()

    try:
        for item in data[:10]:
            crypto = db.query(Cryptocurrency).filter_by(id=item["id"]).first() # verifica se já existe registro da criptomoeda 
            if not crypto:
                # cria instância para tabela cryptocurrencies
                crypto = Cryptocurrency(
                    id=item["id"],
                    name=item["name"],
                    symbol=item["symbol"],
                    rank=int(item["rank"])
                )
                db.add(crypto)
            # cria instância para a tabela market_data
            market_data = MarketData(
                cryptocurrency_id=item["id"],
                price_usd=float(item["priceUsd"]),
                market_cap_usd=float(item["marketCapUsd"]),
                volume_usd_24h=float(item["volumeUsd24Hr"]),
                change_percent_24h=float(item["changePercent24Hr"])
            )
            db.add(market_data)
        db.commit()
        print(f"Dados inseridos com sucesso")
    except Exception as e:
        db.rollback()
        print(f"Erro ao inserir os dados: {e}")
    finally:
        db.close()
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

# Cria classe base para as demais classes
Base = declarative_base()

# Cria classe para a tabela cryptocurrencies (criptomoedas)
class Cryptocurrency(Base):
    __tablename__= "cryptocurrencies"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    symbol = Column(String, nullable=False)
    rank = Column(Integer, nullable=False)

# Cria classe para a tabela market_data (dados de mercado da criptomoeda)
class MarketData(Base):
    __tablename__= "market_data"

    id = Column(Integer, primary_key=True, autoincrement=True)
    cryptocurrency_id = Column(String, ForeignKey("cryptocurrencies.id"), nullable=False)
    price_usd = Column(Float, nullable=False)
    market_cap_usd = Column(Float, nullable=False)
    volume_usd_24h = Column(Float, nullable=False)
    change_percent_24h = Column(Float, nullable=False)
    timestamp = Column(DateTime, server_default=func.now())
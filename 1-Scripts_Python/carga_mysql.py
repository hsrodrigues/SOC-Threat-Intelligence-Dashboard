import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

# Credenciais do .env
usuario = os.getenv('DB_USER')
senha = os.getenv('DB_PASS')
host = os.getenv('DB_HOST')
porta = os.getenv('DB_PORT')
banco = os.getenv('DB_NAME')

df = pd.read_csv('dataset_soc_logs.csv')
engine = create_engine(f"mysql+pymysql://{usuario}:{senha}@{host}:{porta}/{banco}")

# Recriando a tabela bruta
df.to_sql('tb_logs_soc_bruto', con=engine, if_exists='replace', index=False)
print("✅ Tabela 'tb_logs_soc_bruto' recriada no MySQL!")
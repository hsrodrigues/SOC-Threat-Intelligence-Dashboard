import pandas as pd
import numpy as np
from datetime import timedelta, datetime
import random

# Configurações
dias = 30
data_inicial = datetime(2026, 3, 22)
qtd_logs = 5000

paises = ['Brazil', 'United States', 'China', 'Russia', 'Germany', 'North Korea', 'Israel', 'India', 'Ukraine', 'Canada']
tipos_ataque = ['DDoS', 'Brute Force (SSH)', 'SQL Injection', 'Cross-Site Scripting (XSS)', 'Malware Beacon', 'Port Scan']
servidores_alvo = ['SRV-WEB-01', 'SRV-WEB-02', 'SRV-DB-MAIN', 'SRV-DB-REPLICA', 'FIREWALL-EDGE']
status_bloqueio = ['Bloqueado', 'Detectado (Alerta)', 'Falha na Autenticação']

dados = []
for _ in range(qtd_logs):
    data_hora = data_inicial + timedelta(days=random.randint(0, dias-1), hours=random.randint(0, 23), minutes=random.randint(0, 59))
    ataque = np.random.choice(tipos_ataque)
    
    dados.append({
        'Data_Hora': data_hora,
        'IP_Origem': f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}",
        'Pais': random.choice(paises),
        'Tipo_Ataque': ataque,
        'Servidor_Alvo': random.choice(servidores_alvo),
        'Severidade': 'Crítica' if ataque in ['SQL Injection', 'Malware Beacon'] else 'Alta',
        'Acao_Tomada': random.choice(status_bloqueio)
    })

df_soc = pd.DataFrame(dados)
df_soc.to_csv('dataset_soc_logs.csv', index=False)
print("✅ Arquivo 'dataset_soc_logs.csv' criado com sucesso!")
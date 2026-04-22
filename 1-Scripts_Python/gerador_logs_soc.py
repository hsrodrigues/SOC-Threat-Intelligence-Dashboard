import pandas as pd
import numpy as np
from datetime import timedelta, datetime
import random

# 1. Configurações Iniciais do Dataset
dias = 30
data_inicial = datetime(2026, 3, 20) # Começando em março para ter dados recentes
qtd_logs = 5000 # Simulando 5 mil alertas de segurança no mês

# 2. Listas de Mock (Ameaças e Alvos)
tipos_ataque = ['DDoS', 'Brute Force (SSH)', 'SQL Injection', 'Cross-Site Scripting (XSS)', 'Malware Beacon', 'Port Scan']
pesos_ataques = [0.15, 0.30, 0.15, 0.10, 0.05, 0.25] # Probabilidade de cada ataque

servidores_alvo = ['SRV-WEB-01', 'SRV-WEB-02', 'SRV-DB-MAIN', 'SRV-DB-REPLICA', 'FIREWALL-EDGE']
status_bloqueio = ['Bloqueado', 'Detectado (Alerta)', 'Falha na Autenticação']

# Função auxiliar para gerar IPs aleatórios
def gerar_ip_malicioso():
    return f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"

# 3. Gerando os dados iterativamente
dados = []
for _ in range(qtd_logs):
    # Simulando data e hora aleatória dentro dos 30 dias
    data_hora = data_inicial + timedelta(days=random.randint(0, dias-1), hours=random.randint(0, 23), minutes=random.randint(0, 59))
    
    ataque = np.random.choice(tipos_ataque, p=pesos_ataques)
    alvo = random.choice(servidores_alvo)
    
    # Lógica de negócio: SQL Injection geralmente mira banco de dados; Brute Force mira Web/SSH
    if ataque == 'SQL Injection':
        alvo = random.choice(['SRV-DB-MAIN', 'SRV-DB-REPLICA'])
    elif ataque == 'Brute Force (SSH)':
        alvo = random.choice(['SRV-WEB-01', 'SRV-WEB-02'])
        
    # Severidade baseada no ataque
    if ataque in ['SQL Injection', 'Malware Beacon']:
        severidade = 'Crítica'
    elif ataque in ['DDoS', 'Brute Force (SSH)']:
        severidade = 'Alta'
    else:
        severidade = 'Média/Baixa'

    dados.append({
        'Data_Hora': data_hora,
        'IP_Origem': gerar_ip_malicioso(),
        'Tipo_Ataque': ataque,
        'Servidor_Alvo': alvo,
        'Severidade': severidade,
        'Acao_Tomada': random.choice(status_bloqueio)
    })

# 4. Criando e salvando o DataFrame
df_soc = pd.DataFrame(dados)
# Ordenando cronologicamente
df_soc = df_soc.sort_values(by='Data_Hora').reset_index(drop=True)

df_soc.to_csv('dataset_soc_logs.csv', index=False)
print("Logs do SIEM gerados com sucesso! Arquivo: dataset_soc_logs.csv")
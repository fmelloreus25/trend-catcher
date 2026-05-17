import requests
import os
import pandas as pd
from dotenv import load_dotenv

# 1. Credenciais Seguras
load_dotenv()
API_KEY = os.getenv('API_KEY') 

# 2. Lista de Alvos para Escala (Canais concorrentes e referências)
CANAIS_ALVO = [
    'UCX6OQ3DkcsbYNE6H8uQQuVA', # MrBeast
    'UC-lHJZR3Gqxm24_Vd_AJ5Yw', # PewDiePie
    'UCq-Fj5jknLsUf-MWSy4_brA', # T-Series
    'UCRijo3ddMTht_IHyXcQlftA', # Dude Perfect
    'UCBJycsmduvYEL83R_U4JriQ'  # Marques Brownlee (MKBHD)
]

# "Carrinho de compras" para empilhar os dados de cada iteração
linhas_tabela = [] 

print("Iniciando extração em lote dos concorrentes...\n")

# 3. O Loop de Extração Blindado
for canal_id in CANAIS_ALVO:
    url = f'https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id={canal_id}&key={API_KEY}'
    resposta = requests.get(url)
    
    # Verifica falha grave de servidor
    if resposta.status_code == 200:
        dados = resposta.json()
        
        # PROGRAMAÇÃO DEFENSIVA: Verifica se o YouTube realmente mandou a chave 'items'
        if 'items' in dados and len(dados['items']) > 0:
            canal_info = dados['items'][0]
            
            # Extração
            nome = canal_info['snippet']['title']
            inscritos = int(canal_info['statistics']['subscriberCount'])
            views = int(canal_info['statistics']['viewCount'])
            
            # Regra de negócio (KPI)
            kpi = views / inscritos if inscritos > 0 else 0
            
            # Adiciona os dados validados ao nosso carrinho
            linhas_tabela.append({
                'nome_canal': nome,
                'total_inscritos': inscritos,
                'total_visualizacoes': views,
                'kpi_views_por_inscrito': round(kpi, 2)
            })
            print(f"[OK] Dados extraídos: {nome}")
            
        else:
            # O sistema não quebra. Apenas avisa e continua rodando.
            print(f"[ALERTA] Canal não encontrado ou sem dados para o ID: {canal_id}")
            
    else:
        print(f"[ERRO] Falha de conexão ao extrair ID: {canal_id}")

# 4. Transformação Final (ETL - Transform)
# Mandamos o Pandas processar o carrinho cheio e criar a tabela
df_concorrencia = pd.DataFrame(linhas_tabela)

print("\n--- DATAFRAME DE INTELIGÊNCIA COMPETITIVA ---")
print(df_concorrencia)
import os
from dotenv import load_dotenv

# Carrega as credenciais seguras do cofre local
load_dotenv()
API_KEY = os.getenv('API_KEY') 

# Lista de Alvos para Escala
CANAIS_ALVO = [
    'UCX6OQ3DkcsbYNE6H8uQQuVA', # MrBeast
    'UC-lHJZR3Gqxm24_Vd_AJ5Yw', # PewDiePie
    'UCq-Fj5jknLsUf-MWSy4_brA', # T-Series
    'UCRijo3ddMTht_IHyXcQlftA', # Dude Perfect
    'UCBJycsmduvYEL83R_U4JriQ'  # Marques Brownlee
]
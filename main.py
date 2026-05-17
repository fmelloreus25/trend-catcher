# Importando configurações de ambiente
from config.configuracoes import API_KEY, CANAIS_ALVO

# Importando as ferramentas do nosso pipeline
from modulos.extrator import extrair_dados_youtube
from modulos.transformador import estruturar_dataframe
from modulos.carregador import salvar_no_banco

def executar_pipeline():
    # 1. Extração (Extract)
    dados_brutos = extrair_dados_youtube(API_KEY, CANAIS_ALVO)
    
    # 2. Transformação (Transform)
    df_final = estruturar_dataframe(dados_brutos)
    
    # 3. Validação Visual
    print("\n--- DATAFRAME DE INTELIGÊNCIA COMPETITIVA ---")
    print(df_final)
    
    # 4. Carga (Load) - Enviando para o Banco de Dados SQL
    salvar_no_banco(df_final)

if __name__ == "__main__":
    executar_pipeline()
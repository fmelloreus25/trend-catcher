import pandas as pd

def estruturar_dataframe(dados_brutos):
    # Recebe a lista de dicionários e converte em um DataFrame tabular
    df_concorrencia = pd.DataFrame(dados_brutos)
    return df_concorrencia
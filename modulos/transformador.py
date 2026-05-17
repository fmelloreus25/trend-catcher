import pandas as pd
from datetime import datetime

def estruturar_dataframe(dados_brutos):
    # 1. Converte os dados para DataFrame
    df_concorrencia = pd.DataFrame(dados_brutos)
    
    # 2. Captura a data exata de hoje no formato Ano-Mês-Dia (Padrão de Banco de Dados)
    data_atual = datetime.now().strftime('%Y-%m-%d')
    
    # 3. Cria uma nova coluna na tabela e preenche todas as linhas com a data de hoje
    df_concorrencia['data_coleta'] = data_atual
    
    # 4. A Mágica do Sênior: Transforma a coluna 'data_coleta' no Índice (Index) da tabela
    # O inplace=True faz a alteração direto na memória sem precisar criar uma cópia da tabela
    df_concorrencia.set_index('data_coleta', inplace=True)
    
    return df_concorrencia
import sqlite3
import os

def salvar_no_banco(df, nome_tabela="historico_concorrencia", nome_banco="dados/youtube_trends.db"):
    os.makedirs('dados', exist_ok=True)
    conexao = sqlite3.connect(nome_banco)
    try:
        df.to_sql(nome_tabela, conexao, if_exists='append', index=True)
        print(f"\n[SUCESSO] Dados salvos com sucesso na tabela '{nome_tabela}' do banco '{nome_banco}'.")
    except Exception as e:
        print(f"\n[ERRO CRÍTICO] Falha ao salvar no banco de dados: {e}")
    finally:
        conexao.close()
import sqlite3
import pandas as pd

def auditar_banco():
    print("A abrir o cofre de dados SQLite...\n")
    conexao = sqlite3.connect('dados/youtube_trends.db')
    try:
        query = "SELECT * FROM historico_concorrencia"
        df_historico = pd.read_sql(query, conexao)
        
        print("[SUCESSO] Dados extraídos do SQL com sucesso!")
        print(f"Total de registros históricos guardados: {len(df_historico)} linhas.\n")
        print("--- REGISTROS RECUPERADOS DO BANCO DE DADOS (SQL) ---")
        print(df_historico)
    except Exception as e:
        print(f"[ERRO CRÍTICO] Não foi possível ler a tabela SQL: {e}")
    finally:
        conexao.close()

if __name__ == "__main__":
    auditar_banco()
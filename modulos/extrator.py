import requests

def extrair_dados_youtube(api_key, lista_canais):
    linhas_tabela = [] 
    print("Iniciando extração em lote dos concorrentes...\n")

    for canal_id in lista_canais:
        url = f'https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id={canal_id}&key={api_key}'
        resposta = requests.get(url)
        
        if resposta.status_code == 200:
            dados = resposta.json()
            if 'items' in dados and len(dados['items']) > 0:
                canal_info = dados['items'][0]
                
                nome = canal_info['snippet']['title']
                inscritos = int(canal_info['statistics']['subscriberCount'])
                views = int(canal_info['statistics']['viewCount'])
                kpi = views / inscritos if inscritos > 0 else 0
                
                linhas_tabela.append({
                    'nome_canal': nome,
                    'total_inscritos': inscritos,
                    'total_visualizacoes': views,
                    'kpi_views_por_inscrito': round(kpi, 2)
                })
                print(f"[OK] Dados extraídos: {nome}")
            else:
                print(f"[ALERTA] Canal não encontrado para o ID: {canal_id}")
        else:
            print(f"[ERRO] Falha de conexão ao extrair ID: {canal_id}")

    return linhas_tabela
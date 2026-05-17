import requests

# Configuração de credenciais e parâmetros da requisição
API_KEY = 'AIzaSyA8DHMVSVEYQqjqQTvZ_1chC6agHUfXomU' 
CHANNEL_ID = 'UCX6OQ3DkcsbYNE6H8uQQuVA' # ID do canal mapeado (MrBeast)

# Construção do endpoint da YouTube Data API v3
url = f'https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id={CHANNEL_ID}&key={API_KEY}'

# Execução da requisição HTTP GET
resposta = requests.get(url)

# Validação do status e extração de dados
if resposta.status_code == 200:
    dados = resposta.json()
    canal_info = dados['items'][0]
    estatisticas = canal_info['statistics']
    
    # Extração e Casting (Volumetrias brutas)
    inscritos = int(estatisticas['subscriberCount'])
    visualizacoes = int(estatisticas['viewCount'])
    
    # Criação de Métricas Derivadas (KPIs de Negócio)
    views_por_inscrito = visualizacoes / inscritos
    
    # Output estruturado
    print(f"Total de Inscritos: {inscritos}")
    print(f"Total de Visualizações: {visualizacoes}")
    print(f"Engajamento (Views/Inscrito): {views_por_inscrito:.2f}")

else:
    print(f"Falha na requisição. Status Code: {resposta.status_code}")
# Trend Catcher: Inteligência Competitiva na Creator Economy

O **Trend Catcher** é uma infraestrutura automatizada de dados (Pipeline ETL) projetada para capturar, estruturar e analisar métricas de performance de canais de criadores de conteúdo em tempo real. O objetivo principal é eliminar a latência e a dependência de relatórios manuais, centralizando indicadores cruciais para suporte à tomada de decisão analítica em agências de grande porte.

---

## 1. O Problema de Negócio

No ecossistema atual de produção de conteúdo, diretores de estratégia e inteligência competem pela atenção da audiência em tempo real. Tomar decisões editoriais baseando-se em planilhas CSV/XLSX baixadas manualmente uma vez por semana gera atrasos operacionais. 

O projeto resolve esse gargalo estabelecendo um duto automatizado diretamente conectado aos servidores de dados do YouTube. O pipeline monitora canais concorrentes de larga escala, calculando indicadores derivados de eficiência de audiência e armazenando esses dados como **Séries Temporais** para análises longitudinais de viralidade.

---

## 2. Arquitetura Modular do Pipeline (ETL)

O projeto segue os princípios de separação de responsabilidades e programação defensiva, estruturado nas seguintes camadas:

* **[E] Ingestão em Lote:** Módulo (`extrator.py`) responsável por iterar sobre listas de alvos, comunicar-se via protocolo HTTP com a API RESTful do Google Cloud e isolar canais fora do ar (Programação Defensiva).
* **[T] Transformação de Dados:** Módulo (`transformador.py`) que processa o JSON cru em memória RAM utilizando `pandas`, realizando *casting* de tipos, estruturando colunas matemáticas e ancorando as matrizes com índices de datas de coleta.
* **[L] Persistência Histórica:** Módulo (`carregador.py`) encarregado de injetar os DataFrames higienizados em um banco de dados relacional e portátil `SQLite3`, acumulando o histórico diário da concorrência sem sobrescrever dados.
* **Orquestração e Segurança:** Um arquivo principal (`main.py`) coordena o fluxo, enquanto credenciais críticas ficam protegidas em nível de máquina através de cofres `.env`.

---

## 3. Estrutura do Repositório

```text
├── config/
│   └── configuracoes.py    # Listas de monitoramento e cofre de credenciais
├── modulos/
│   ├── extrator.py         # Módulo de requisições HTTP (API YouTube)
│   ├── transformador.py    # Módulo de modelagem relacional via Pandas
│   └── carregador.py       # Módulo de injeção em banco de dados SQL
├── dados/
│   └── youtube_trends.db   # Banco de Dados Histórico Local (Gerado via código)
├── .env                    # Variáveis sensíveis (Bloqueado por segurança)
├── .gitignore              # Filtro de auditoria (Cofres, Caches e Temporários)
├── main.py                 # Maestro/Orquestrador do Pipeline ETL
└── README.md               # Documentação Executiva
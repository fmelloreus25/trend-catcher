# Trend Catcher: Inteligência Competitiva na Creator Economy

O **Trend Catcher** é uma infraestrutura automatizada de dados (Pipeline ETL) projetada para capturar, estruturar e analisar métricas de performance de canais de criadores de conteúdo em tempo real. O objetivo principal é eliminar a latência e a dependência de relatórios manuais (como exportações do YouTube Studio), centralizando indicadores cruciais para suporte à tomada de decisão analítica em agências de grande porte.

---

## 1. O Problema de Negócio

No ecossistema atual de produção de conteúdo, diretores de estratégia e inteligência competem pela atenção da audiência em tempo real. Tomar decisões editoriais ou de contratação baseando-se em planilhas CSV/XLSX baixadas manualmente uma vez por semana gera atrasos operacionais. 

O projeto resolve esse gargalo ao estabelecer um duto automatizado diretamente conectado aos servidores de dados. Como caso de estudo prático, o pipeline monitora criadores de larga escala (como o canal *MrBeast*), extraindo volumetrias brutas e calculando indicadores derivados de eficiência de audiência para identificar proativamente padrões de crescimento e viralidade.

---

## 2. Arquitetura Técnica do Pipeline

O projeto foi desenhado seguindo os padrões modernos de Engenharia de Analytics, dividido nas seguintes camadas:

* **Extração (Ingestão):** Consumo automatizado da API RESTful do Google (YouTube Data API v3) via requisições HTTP (`requests`) em Python 3.
* **Segurança & Governança:** Isolamento de credenciais críticas de nuvem utilizando variáveis de ambiente (`.env`) e políticas rígidas de bloqueio de versionamento com `.gitignore`.
* **Isolamento de Ambiente:** Utilização de ambientes virtuais (`venv`) para governança de dependências e bibliotecas do projeto.
* **Próximas Fases:** Estruturação tabular de dados em memória RAM (`pandas`) e persistência relacional em banco de dados local (`SQLite`).

---

## 3. Estrutura do Repositório

```text
├── venv/                 # Ambiente virtual isolado do Python
├── .env                  # Cofre local de credenciais (Não versionado por segurança)
├── .gitignore            # Filtro de arquivos bloqueados para o Git
├── README.md             # Documentação executiva do projeto
└── teste_api.py          # Script de ingestão e validação do pipeline
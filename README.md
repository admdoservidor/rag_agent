# ragda

Assistente baseado em RAG (Retrieval-Augmented Generation) que consome a documentação do LangChain e responde perguntas utilizando LLMs da Groq.

## Sobre

O **ragda** é um projeto em Python que:

- Faz download e indexa páginas da documentação do LangChain/DeepAgents/LangGraph.
- Gera embeddings com o modelo `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`.
- Armazena os chunks em um banco vetorial **Chroma** (persistido em `.db/`).
- Permite consultar a base de conhecimento por meio de um agente de IA com LLMs da **Groq**.

## Estrutura do projeto

```
ragda/
├── .env                  # Variáveis de ambiente (não versionar)
├── .env.example          # Exemplo de variáveis de ambiente
├── .gitignore            # Arquivos e pastas ignorados pelo Git
├── pyproject.toml        # Configuração e dependências do projeto
├── uv.lock               # Lockfile do uv
├── README.md             # Este arquivo
├── src/
│   └── ragda/
│       ├── __init__.py
│       ├── main.py       # Ponto de entrada do agente
│       ├── db_create.py  # Criação e indexação do banco vetorial
│       ├── agents/       # Definição do agente
│       ├── core/         # Lógica de negócio
│       ├── docs/         # Documentação interna
│       ├── llm/          # Configuração de modelos LLM
│       └── tools/        # Ferramentas disponíveis ao agente
└── .db/                  # Banco vetorial Chroma (gerado, não versionar)
```

## Requisitos

- Python >= 3.11
- [uv](https://github.com/astral-sh/uv) (recomendado) ou pip

## Instalação

Clone o repositório e instale as dependências:

```bash
# com uv
uv sync

# ou com pip
pip install -e .
```

## Configuração

Copie o arquivo de exemplo para criar o seu `.env`:

```bash
cp .env.example .env
```

Em seguida, edite o `.env` e insira sua chave da Groq:

```env
GROQ_API_KEY = gsk_sua_chave_aqui
```

> ⚠️ Nunca commite o arquivo `.env` contendo chaves reais. Ele já está ignorado pelo `.gitignore`.

## Uso

### Indexar a documentação (criar o banco vetorial)

```bash
python -m ragda.db_create
```

### Executar o agente

```bash
python -m ragda.main
# ou, se instalado como script:
ragda
```

## Dependências principais

- `deepagents` — agente com suporte a subagentes e streaming
- `langchain`, `langchain-core`, `langchain-chroma`, `langchain-groq`, `langchain-huggingface`, `langchain-text-splitters`
- `sentence-transformers` — embeddings
- `chromadb` — banco vetorial Chroma
- `requests` — requisições HTTP para baixar a documentação

## Licença

Este projeto está sob a licença MIT.

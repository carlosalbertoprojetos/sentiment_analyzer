# Analisador de Sentimentos - FastAPI

API que analisa o sentimento de um texto informado pelo usuário, classificando como **positivo**, **negativo** ou **neutro**.

**Objetivo:** Demonstrar como integrar processamento de linguagem natural (NLP) com FastAPI, além de aplicar middleware personalizado para log de requisições.

---

## Funcionalidades
- Analisar o sentimento de um texto
- Middleware para log de requisições

---

## Dependências
- `fastapi`: Framework da API.
- `uvicorn`: Servidor para execução local.
- `textblob`: Biblioteca NLP para análise de sentimentos.

---

## Endpoints
- `POST /analyze` – Recebe um texto e retorna o sentimento analisado

---

## Instalação e configuração

### 1. Acesse a pasta do projeto
```bash
cd sentiment_analyzer_senior
```

### 2. (Opcional) Crie um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate        # Windows
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Baixe os dados necessários para o TextBlob
```bash
python -m textblob.download_corpora
```

---

## Como executar
```bash
uvicorn main:app --reload
```

Acesse: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Requisitos

- Python 3.8 ou superior
- pip instalado

---

## Interface Swagger

A FastAPI gera uma interface interativa para testar todos os endpoints automaticamente, acessível em:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
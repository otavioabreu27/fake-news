# fake-news

P1 e P2 LDDM

## 🧪 Sobre o projeto

Este projeto realiza a classificação de notícias como **FAKE** ou **REAL** utilizando um modelo baseado em BERT.

## 🚀 Como rodar

Certifique-se de ter o **Docker** e o **Docker Compose** instalados.

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/fake-news.git
cd fake-news
````

### 2. Suba a aplicação

```bash
docker-compose up --build
```

### 3. Acesse no navegador

A aplicação estará disponível em:

➡️ [http://localhost:3000](http://localhost:3000)

## 🐳 Serviços

* **Frontend (React + Vite)**: Porta `3000`
* **Backend (FastAPI + Transformers)**: Porta `8000` (internamente)

```
📦 fake-news
├── fake-news-api      # Backend com FastAPI
├── fake-news-ui       # Frontend com React
├── docker-compose.yml
└── README.md
```

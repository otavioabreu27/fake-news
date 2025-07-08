# Imagem base
FROM python:3.11-slim

# Variáveis de ambiente para evitar prompts do transformers e logs desnecessários
ENV TRANSFORMERS_NO_TF=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Diretório de trabalho
WORKDIR /app

# Copia os arquivos
COPY requirements.txt .
RUN apt-get update && apt-get install -y python3-dev build-essential libxml2-dev libxslt-dev libjpeg-dev zlib1g-dev libcurl4-openssl-dev libssl-dev && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get purge -y --auto-remove && \
    rm -rf /var/lib/apt/lists/*

# Copia o restante do código
COPY . .

# Comando para rodar o servidor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

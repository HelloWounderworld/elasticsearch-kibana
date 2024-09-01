# Usar a imagem base do Ubuntu
FROM ubuntu:20.04

# Definir variáveis de ambiente
ENV DEBIAN_FRONTEND=noninteractive

# Atualizar o sistema e instalar dependências
RUN apt-get update && \
    apt-get install -y python3 python3-pip curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Instalar a biblioteca Elasticsearch
RUN pip3 install elasticsearch

RUN pip3 freeze > requirement.txt

# Criar um diretório de trabalho
WORKDIR /app

# Copiar o código Python para o contêiner (se você tiver um script)
COPY teste_elasticsearch.py .

# Comando padrão (substitua pelo seu script se necessário)
CMD ["python3"]

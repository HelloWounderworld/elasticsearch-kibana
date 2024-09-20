# Elastic Search - Kibana
This repository is to understand about elastic search and how to use Docker compose to use Kibana!

    https://www.elastic.co/docs

    https://www.elastic.co/guide/en/elasticsearch/reference/current/elasticsearch-intro.html

    https://www.elastic.co/pt/kibana

## Using Elastic Search installing by pip:
Para usar a biblioteca elasticsearch do Python, é necessário que o Elasticsearch esteja instalado e em execução em um servidor, seja localmente ou em um servidor remoto. Aqui estão os pontos principais:

- 1. O que é o Elasticsearch?
O Elasticsearch é um mecanismo de busca e análise de dados distribuído e em tempo real. Para interagir com ele através do Python, você precisa ter uma instância do Elasticsearch ativa.

- 2. Instalação do Elasticsearch
Se você ainda não instalou o Elasticsearch, você pode fazê-lo seguindo as instruções da documentação oficial. Aqui estão algumas opções comuns:

    - Linux: Você pode usar pacotes .deb ou .rpm.
    - Docker: Usar uma imagem do Elasticsearch.
    - Windows: Baixar e instalar o Elasticsearch como um serviço.

- 3. Iniciar o Elasticsearch
Após a instalação, você precisa iniciar o serviço. Dependendo do método de instalação, isso pode ser feito com:

    - Linux: If you have elasticsearch insataled localy
        
            sudo service elasticsearch start

    - Docker: If you can access elastic search remotly

            docker run -d -p 9200:9200 --name elasticsearch elasticsearch:7.10.0

- 4. Verificar se o Elasticsearch está em Execução

    Depois de iniciar o Elasticsearch, verifique se ele está funcionando corretamente acessando:

        curl -X GET "http://localhost:9200/"

    Você deve receber uma resposta JSON com informações sobre o cluster.

- 5. Conectar-se ao Elasticsearch com Python

    Uma vez que o Elasticsearch esteja em execução, você pode usar a biblioteca elasticsearch do Python para interagir com ele, como no exemplo anterior.

### Resumo
Sim, você precisa de uma instância do Elasticsearch em execução para usar a biblioteca elasticsearch do Python.
Instale e inicie o Elasticsearch antes de tentar indexar ou consultar dados.

### Step by step
Create a virtual enviromment going in your directory

    python -m venv name_project or python3 -m venv name_project

Tip: You need to install "venv" using

    apt-get install python(your.python.version)-venv

Now, you have to to activate the virtual enviromment

    source name_enviromment/bin/activate

With the enviromment on you can install packages

    pip install package_name

To check if your package was installed using the following command

    pip list

Now, you have to configure the port to the localhost

    python3 -m http.server 8000

Or just run the file

    python3 server.py

Save some data to the elastic search activating python script

    python3 teste_elasticsearch.py

Check using curl if the data was saved

    curl -X GET "http://localhost:9200/test-index/_doc/1"

When you finish your job, you can off your virtual enviromment using the following command

    deactivate

## Using Elastic Search installing by docker compose using kibana:
In first place, you have to configure the docker compose using kibana.

After setting docker compose file it use following command

    docker compose up -d --build

If you want to stop and remove all the container created just this directory, type following command

    docker compose down

Test using curl if Kibana's elasticsearch is working

    curl -X POST "http://localhost:9200/test-index/_doc/1" -H 'Content-Type: application/json' -d '{"author": "Alice","text": "Elasticsearch é incrível!","timestamp": "2024-09-01T00:00:00"}'

Check if data was saved

    curl -X GET "http://localhost:9200/test-index/_doc/1"

If was returned any json that show data that you saved, then this it mens is working.

After installation, you can see the documentation of kibana to learn how to use

    https://www.elastic.co/guide/en/kibana/7.9/index.html

 Limpar os Dados do Elasticsearch
Se você não precisa dos dados existentes e pode começar do zero, você pode limpar o volume de dados que está sendo usado pelo Elasticsearch. Para fazer isso:

Pare os contêineres:

Copiar
docker-compose down
Remova o volume que contém os dados do Elasticsearch. Você pode fazer isso com o seguinte comando:

Copiar
docker volume rm <nome_do_volume>
No seu caso, o volume é chamado esdata, então você pode usar:

Copiar
docker volume rm elasticsearch-kibana_esdata
Inicie novamente os contêineres:

Copiar
docker-compose up

## More like this query

    git@github.com:HelloWounderworld/elasticsearch-kibana.git

## D3 gallery

    https://observablehq.com/@d3/gallery

## More complete Elasticsearch and Kibana

    https://github.com/sherifabdlnaby/elastdocker/blob/main/docker-compose.yml

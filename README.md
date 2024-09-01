# Elastic Search - Kibana
This repository is to understand about elastic search and how to use Docker compose to use Kibana!

## Using Elastic Search installing by pip:
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

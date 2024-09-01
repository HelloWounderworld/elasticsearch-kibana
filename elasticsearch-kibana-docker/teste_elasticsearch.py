import time
from elasticsearch import Elasticsearch, ConnectionError

# Conectar ao Elasticsearch com uma espera
es = Elasticsearch([{'scheme': 'http', 'host': 'localhost', 'port': 9200}])

# Verificar se a conexão está funcionando
while True:
    try:
        if es.ping():
            print("Conexão bem-sucedida!")
            break
    except ConnectionError:
        print("Falha na conexão. Tentando novamente...")
        time.sleep(5)  # Espera 5 segundos antes de tentar novamente

# Indexar um documento
doc = {
    'author': 'Alice',
    'text': 'Elasticsearch é incrível!',
    'timestamp': '2024-09-01T00:00:00'
}
res = es.index(index='test-index', id=1, body=doc)
print(res['result'])

# Buscar um documento
res = es.get(index='test-index', id=1)
print(res['_source'])

# Realizar uma busca
res = es.search(index='test-index', body={'query': {'match': {'author': 'Alice'}}})
print(res['hits']['hits'])
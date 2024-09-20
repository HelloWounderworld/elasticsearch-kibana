from elasticsearch import Elasticsearch

# Conectar ao Elasticsearch
es = Elasticsearch([{'scheme': 'http', 'host': 'localhost', 'port': 9200}], headers={'Content-Type': 'application/json'})

# Verificar se a conexão está funcionando
if es.ping():
    print("Conexão bem-sucedida!")
else:
    print("Falha na conexão.")

# Indexar um documento
doc = {
    'author': 'Alice',
    'text': 'Elasticsearch é incrível!',
    'timestamp': '2024-09-01T00:00:00'
}

# Indexar o documento
res = es.index(index='test-index', id=1, body=doc)
print(res['result'])

# Buscar um documento
res = es.get(index='test-index', id=1)
print(res['_source'])

# Realizar uma busca
res = es.search(index='test-index', body={'query': {'match': {'author': 'Alice'}}})
print(res['hits']['hits'])
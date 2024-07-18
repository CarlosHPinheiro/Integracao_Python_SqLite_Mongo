from pymongo import MongoClient
from mongo.sql_alchemy.sql_alchemy_app import criar_docs

# Criando a Conexão no MongoDB
connection_string = "mongodb+srv://<user>:<password>@cluster0.pvsagyb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(connection_string)

# Criando o banco de dados e a coleção
db = client.bank
collections = db.contas


def criar_documentos():
    documents = criar_docs()
    results = collections.insert_many(documents)
    print(f"Documentos inseridos no MongoDB com os IDs: {results.inserted_ids}")


def buscar_doc(chave, valor):
    results = collections.find({chave: valor})
    for result in results:
        print(result)


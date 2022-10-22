from http import client
from pymongo import MongoClient as mc 


client = mc('mongodb://localhost:27017')

db = client.get_database('dbProjetos')

collection = db.get_collection('Test')

pergunta = input('Digite o número do lote corretamente').strip()

result = collection.find_one({'LOTE': pergunta })

if result: 
    print('O LOTE FOI ENCONTRADO !!')
    print(result)

else :
    print('O LOTE NÃO FOI ENCONTRADO !!')
    print('')







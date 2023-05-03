from bson import BSON, json_util  # Libreria para codificar y decodificar JSON to BSON
from pymongo import MongoClient
from bson.raw_bson import RawBSONDocument
import bsonjs  # Una libreria para convertir entre BSON y MongoDB JSON extendido

# JSON to BSON
bson_example = BSON.encode({"Hello": "World"})
print(bson_example)
# BSON to JSON
json_example = BSON.decode(bson_example)
print(json_example)
# b'\x16\x00\x00\x00\x02Hello\x00\x06\x00\x00\x00World\x00\x00'
# {'Hello': 'World'}

# bsonjs -> Un convertidor rápido de BSON a MongoDB Extended JSON para Python

# JSON to BSON
bson_bytes = bsonjs.loads('{"hello": "world"}')
print(type(bson_bytes))
print(bson_bytes)
# BSON to JSON
json_example = bsonjs.dumps(bson_bytes)
print(json_example)

# '{ "hello" : "world" }'
# '\x16\x00\x00\x00\x02hello\x00\x06\x00\x00\x00world\x00\x00'

# BSON to Mongo
client = MongoClient("localhost", 27017, document_class=RawBSONDocument)
db = client.ejemplomongo
# bson_bytes = bsonjs.loads('{"_id": 1, "x": 2}')
bson_bytes = bsonjs.loads('{"Hola": "Pepito bb", "x": 2}')
print(bson_bytes)
# insertar documentos
result = db.prueba.insert_one(RawBSONDocument(bson_bytes))
result.inserted_id  # NOTE: inserted_id is None
print(result.acknowledged)
# buscar documentos en mongo
raw_doc = db.prueba.find_one({'x': 2})
print(raw_doc.raw)
print(raw_doc.raw == bson_bytes)
bsonjs.dumps(raw_doc.raw)

# Encontrar colecciones
print(f'La colección prueba tiene la siguientes colecciones')
print(db.prueba.find())

import json
from bson import BSON
import bsonjs
from crud_bson_functions import BasicBsonCRUD

documents = [
    {"nombre": "David", "edad": 20},
     {"nombre": "Camilo", "edad": 24},
     {"nombre": "Juan", "edad": 24},
     {"nombre": "Leidy", "edad": 25},
     {"nombre": "Luis", "edad": 31},
     {"nombre": "Pedro", "edad": 40}
]

# Para trabajar con archivos bson
crud = BasicBsonCRUD(name_database="CRUD", name_collection="BSON")

# Crear
"""
json_document = json.dumps({"nombre": "Pepito", "edad": 32})
bson_byte = bsonjs.loads(json_document)
crud.crear_uno(bson_byte)

"""
# crud.crear_muchos(documents) # Funciona con json pero no con bson

# Convertir cada documento json en bson
"""bson_bytes = []
for document in documents:
    document_json = json.dumps(document)
    bson_byte = bsonjs.loads(document_json)
    bson_bytes.append(bson_byte)


# Enviar uno por uno a la base de datos

for bson_byte in bson_bytes:
    crud.crear_uno(bson_byte)
"""


"""documents2 = [
    {"_id": 1, "nombre": "Pepito", "edad": 35},
    {"_id": 2, "nombre": "Pepito", "edad": 45},
    {"_id": 3, "nombre": "Pepito", "edad": 78},
    {"_id": 4, "nombre": "Pepito", "edad": 90},
    {"_id": 5, "nombre": "Pepito", "edad": 10}
]

bson_bytes = []
for document in documents2:
    document_json = json.dumps(document)
    bson_byte = bsonjs.loads(document_json)
    bson_bytes.append(bson_byte)


# Enviar uno por uno a la base de datos

for bson_byte in bson_bytes:
    crud.crear_uno(bson_byte)"""

# Read (find)

# crud.leer_uno({"edad":20})
# crud.leer_uno({"edad": {"$gt": 30}})

# crud.leer_muchos({}) # Sin criterio nos devuelve todos los objetos
# crud.leer_muchos({"edad": {"$lt": 30}})
# crud.leer_muchos({"edad": {"$eq": 32}})
# crud.leer_muchos({"edad": {"$gt": 25}})
# crud.leer_muchos({"edad": {"$gte": 19, "$lte": 40}})

# Actualizar
# crud.actualizar_uno(criterio={"nombre": "Camilo"}, replace_by={"$set": {"edad": 30}})
#crud.leer_muchos({})
# crud.actualizar_muchos(criterio={"nombre": "Pepito"}, replace_by={"$set": {"edad": 30}})
#crud.leer_muchos({"nombre": "Pepito"})

# Delete
# crud.borrar_uno({"nombre": "Juan"})
# crud.borrar_muchos({"nombre": "Pepito"})

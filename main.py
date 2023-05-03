import json
from bson import BSON
import bsonjs
from crud_functions import BasicCRUD, BasicBsonCRUD

documents = [
    {"nombre": "David", "edad": 20},
    {"nombre": "Camilo", "edad": 24},
    {"nombre": "Juan", "edad": 24},
    {"nombre": "Leidy", "edad": 25},
    {"nombre": "Luis", "edad": 33},
    {"nombre": "Pedro", "edad": 40}
]

# Para trabajar con archivos json
# crud = BasicBsonCRUD(name_database="CRUD", name_collection="BSON")
# Para trabajar con archivos bson
# crud = BasicCRUD(name_database="CRUD", name_collection="JSON")

# Create (insert)
    # Descomentar cuando se use BasicBsonCrud
"""# Convertir cada documento json en bson
bson_bytes = []
for document in documents:
    document_json = json.dumps(document)
    bson_byte = bsonjs.loads(document_json)
    bson_bytes.append(bson_byte)
# Enviar uno por uno a la base de datos
for bson_byte in bson_bytes:
    crud.create_one(bson_byte)"""

    # Descomentar cuando se use BasicCrud
# crud.create_many(document) # Funciona con json pero no con bson

# crud.create_one({"nombre": "Pepito", "edad": 32})
"""crud.create_one({"_id": 1, "nombre": "Pepito", "edad": 32})
crud.create_one({"_id": 2, "nombre": "Pepito", "edad": 45})
crud.create_one({"_id": 3, "nombre": "Pepito", "edad": 78})
crud.create_one({"_id": 4, "nombre": "Pepito", "edad": 90})
crud.create_one({"_id": 5, "nombre": "Pepito", "edad": 10})"""

# Read (find)
# crud_bson.read_many({"edad": {"$lt": 30}})
# crud.read_many({"edad": {"$eq": 32}})
# crud.read_many({"edad": {"$gt": 25}})
# crud.read_many({ "edad": {"$gte": 19, "$lte": 40}})
# crud2.read_many({"edad": {"$eq": 33}})  # Sin criterio nos devuelve todos los objetos

# crud.read_one({"edad":20})
# crud.read_one({"edad": {"$gt": 30}})

# Delete
# crud.delete_one_doc({"nombre": "Juan"})
# crud.delete_many_doc({"nombre": "Luis"})

# Actualizar
# crud.update_one_doc(criterio={"nombre": "Camilo"}, replace_by={"$set": {"edad": 30}})
# crud.read_many({})
# crud.update_many_doc(criterio={"nombre": "Pepito"}, replace_by={"$set": {"edad": 30}})
# crud.read_many({"nombre": "Pepito"})

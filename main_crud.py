from crud_functions import BasicCRUD

documents = [
    {"nombre": "David", "edad": 20},
    {"nombre": "Camilo", "edad": 24},
    {"nombre": "Juan", "edad": 24},
    {"nombre": "Leidy", "edad": 25},
    {"nombre": "Luis", "edad": 31},
    {"nombre": "Pedro", "edad": 40},
    {"nombre": "Pedro", "edad": 40}
]

crud = BasicCRUD(name_database="CRUD", name_collection="JSON")

# Crear documento en la colección
#crud.crear_uno({"nombre": "Kevin", "edad": 14})
# crud.crear_muchos(documents)

# crud.leer_uno({'nombre': 'Kevin'})
# crud.leer_uno({"edad":20})

# crud.leer_muchos({'nombre': 'kevin'}) # Sin criterio nos devuelve todos los objetos
# crud.leer_muchos({})
# crud.leer_muchos({"edad": {"$lte": 25}})
# crud.leer_muchos({"edad": {"$eq": 22}})
# crud.leer_muchos({"edad": {"$gt": 25}})
# crud.leer_muchos({ "edad": {"$gte": 19, "$lte": 40}})

# crud.actualizar_uno(criterio={"nombre": "Camilo"}, replace_by={"$set": {"edad": 30}})
# crud.actualizar_uno(criterio={"edad": {"$gte": 25}}, replace_by={"$set": {"edad": 30}})

# crud.actualizar_muchos(criterio={"nombre": "kevin"}, replace_by={"$set": {"edad": 25}})

# crud.borrar_uno({"nombre": "Kevin"})
#crud.borrar_muchos({"edad": {"$gte": 25}})
#crud.leer_muchos({})
# crud.borrar_muchos({"nombre": {"$in": ['Cam']}})

# crud.leer_muchos({'$and' : [{'nombre':'Kevin'}, {'edad':22}]})
# crud.leer_muchos({'$and' : [{'nombre':'Kevin'}, {"edad": {"$lte": 25}}]})
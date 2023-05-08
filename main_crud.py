from crud_functions import BasicCRUD

documents = [
    {"nombre": "David", "edad": 20},
    {"nombre": "Camilo", "edad": 24},
    {"nombre": "Juan", "edad": 24},
    {"nombre": "Leidy", "edad": 25},
    {"nombre": "Luis", "edad": 31},
    {"nombre": "Pedro", "edad": 40},
    {"nombre": "Pedro", "edad": 35}
]

crud = BasicCRUD(name_database="CRUD", name_collection="JSON")

# Crear documento en la colección
# crud.crear_uno({"nombre": "Pepito", "edad": 45})
# crud.crear_uno(documents) # Esto no va a funcionar!!!
# crud.crear_muchos(documents)

# crud.leer_uno({'nombre': 'Pedro'})
# crud.leer_uno({"edad":20})

# crud.leer_muchos({'nombre': 'Pedro'})
# crud.leer_muchos({}) # Sin criterio nos devuelve todos los objetos
# crud.leer_muchos({"edad": {"$lte": 25}})
# crud.leer_muchos({"edad": {"$lt": 25}})
# crud.leer_muchos({"edad": {"$eq": 31}})
# crud.leer_muchos({"edad": {"$gt": 25}})
# crud.leer_muchos({ "edad": {"$gte": 19, "$lte": 35}})
# crud.leer_muchos({'$and' : [{'nombre':'Pepito'}, {'edad':14}]})
# crud.leer_muchos({'$and' : [{'nombre':'Pepito'}, {"edad": {"$lte": 25}}]})

# crud.actualizar_uno(criterio={"nombre": "Pedro"}, replace_by={"$set": {"edad": 30}})
# crud.actualizar_uno(criterio={"edad": {"$gte": 25}}, replace_by={"$set": {"edad": 30}})

# crud.actualizar_muchos(criterio={"nombre": "Pedro"}, replace_by={"$set": {"edad": 25}})

# crud.borrar_uno({"nombre": "Pedro"})
# crud.borrar_muchos({"edad": {"$gte": 25}})
# crud.leer_muchos({})
# crud.borrar_muchos({"nombre": {"$in": ['Camilo']}})



from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["name_database"]
collection = db["name_collection"]
collection2 = db["name_collection 2"]

db.collection.insert_one({
    "name": "Homero",
    "orderdate": "3/05/2023",
    "species": "Human",
    "ownerAddress": "Avenida Siempreviva 742",
    "gordo": True
})
db.collection2.insert_one({
    "name": "Marge",
    "orderdate": "3/05/2023",
    "species": "Human",
    "ownerAddress": "Avenida Siempreviva 742",
    "gordo": True
})

response = db.collection.find({})
print(response)
from pymongo import MongoClient
client = MongoClient('localhost',27017)  # 27017 is the default port number for mongodb
db = client.test
col = db.person

db.SalesDB.insert_one({
    "name": "Homero",
    "orderdate": "3/05/2023",
    "species": "Human",
    "ownerAddress": "Avenida Siempreviva 742",
    "gordo": True
})


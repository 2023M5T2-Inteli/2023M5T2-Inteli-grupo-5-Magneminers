import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://Gabi-Barretto:DarthVader01@modulo5.ftovxoa.mongodb.net/?retryWrites=true&w=majority")
db = cluster["Ensaios"]
collection = db["Ensaios"]

def criar_ensaio(e, cic, vrr):
    collection.insert_one({"_id": e, "cic": cic, "vrr": vrr})
    return print("Ensaio criado com sucesso")

def update_ensaio_b1(x, y, z, e):
    collection.update_one({"_id": e}, {"$set": {"x1": x, "y1": y, "z1": z}})
    return print("B1 Atualizado")

def update_ensaio_b2(x, y, z, e):
    collection.update_one({"_id": e}, {"$set":  {"x2": x, "y2": y, "z2": z}})
    return print("B2 Atualizado")

def update_ensaio_b3(x, y, z, e):
    collection.update_one({"_id": e}, {"$set":  {"x3": x, "y3": y, "z3": z}})
    return print("B3 Atualizado")

def update_ensaio_b1_e(x, y, e):
    collection.update_one({"_id": e}, {"$set":  {"x1_e": x, "y1_e": y}})
    return print("B1_e Atualizado")

def update_ensaio_b2_e(x, y, e):
    collection.update_one({"_id": e}, {"$set":  {"x2_e": x, "y2_e": y}})
    return print("B2_e Atualizado")

def update_ensaio_b3_e(x, y, e):
    collection.update_one({"_id": e}, {"$set":  {"x3_e": x, "y3_e": y}})
    return print("B3_e Atualizado")


def encontra_ensaio(e): 
    ensaio = collection.find_one({"_id": e}) 
    return ensaio



#Principal, Cria novo field no documento
#collection.update_one({"_id": 1}, {"$set": {"mdeus": "Funciona"}})


#collection.delete_one({"_id": 0})

#collection.delete_one({"_id": 0})

#limpa o banco CUIDADO
#collection.delete_many({})

# u = collection.find({"_id": 0}) 
# for us in u:
#     print(us)

# u = collection.find_one({"_id": 0})
# print(u)

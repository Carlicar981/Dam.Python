import json

import pymongo
from pymongo import MongoClient
dbStringConnection = 'mongodb://carlos:j%3E%24mfOih@cadox8.es:27017/?authSource=carlos'
client = pymongo.MongoClient(dbStringConnection)
db = client['carlos']  # Replace mongo db name
collection_name = 't'  # Replace mongo db collection name
dbc = db[collection_name]

# Get the data from JSON file
with open('cars.json', 'r') as data_file:
    file_data = json.load(data_file)



dbc.insert_many(file_data)

client.close()

"""def velocidad():
    print("caballos")
    query = {"Model":{"$regex":""},"Horsepower":{"$regex":""},"Acelerate":{"$regex":""}}
    for velo in dbc.find(query).sort("Horsepower",-1):
        print(velo)

velocidad()"""
import csv
import json
import pymongo

dbStringConnection = 'mongodb://carlos:j%3E%24mfOih@cadox8.es:27017/?authSource=carlos'
client = pymongo.MongoClient(dbStringConnection)
db = client['carlos']
collection_name = 't'
dbc = db[collection_name]


csvFile = r'cars.csv'
jsonFile= r'cars.json'

def pasarCsvJson(csvFile, jsonFile):
    jsonArray = []

    
    with open(csvFile, encoding='utf-8') as csvf:
      
        csvReader = csv.DictReader(csvf)

        for row in csvReader:
        
            jsonArray.append(row)

   
    with open(jsonFile, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)



def insertarDatos():
    with open('cars.json', 'r') as data_file:
        file_data = json.load(data_file)

    dbc.insert_many(file_data)

    client.close()

def velocidad():

    print("Coches ordenados caballos")

    for velo in dbc.find({},{"Model": 1,"Horsepower": 1,"Accelerate": 1}).sort([('Horsepower',-1)]):
        print(velo)



def main():
    pasarCsvJson(csvFile,jsonFile)
    insertarDatos()
    velocidad()

main();
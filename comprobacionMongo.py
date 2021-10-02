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

def pasarCsv(csvFile, jsonFile):
    jsonArray = []

    # read csv file
    with open(csvFile, encoding='utf-8') as csvf:
        # load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf)

        # convert each csv row into python dict
        for row in csvReader:
            # add this python dict to json array
            jsonArray.append(row)

    # convert python jsonArray to JSON String and write to file
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
    pasarCsv(csvFile,jsonFile)
    insertarDatos()
    velocidad()

main();
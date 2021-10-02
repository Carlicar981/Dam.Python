import csv
import pymongo

csvFileName = 'cars.csv'

dbStringConnection = 'mongodb://carlos:j%3E%24mfOih@cadox8.es:27017/?authSource=carlos'
dbName = 'carlos'
dbCollection = 't'

def csvReadAndInsertIntoMongoDB():
    client = pymongo.MongoClient(dbStringConnection)
    db = client[dbName]
    cars = db[dbCollection]
    cars.drop()

    with open(csvFileName) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)
            cars.insert_one(row)

def readCarsModels():
    client = pymongo.MongoClient(dbStringConnection)
    db = client[dbName]
    cars = db[dbCollection]

    for car in cars.find({},{"_id":1,"Model":1,"Year":1}):
        print(car)
def main():
    csvReadAndInsertIntoMongoDB()

main();
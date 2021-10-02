import jsonMongo

def velocidad():
    print("nombre")
    query = {"nombre":{"$regex":""}}
    for velo in jsonMongo.dbc.find(query).sort("edad",-1):
        print(velo)

velocidad()
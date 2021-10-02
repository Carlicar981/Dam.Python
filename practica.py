import csv

def insertarDatos():
    with open('cars.json', 'r') as data_file:
        file_data = json.load(data_file)

    dbc.insert_many(file_data)

    client.close()


def main():
    insertarDatos()

main()
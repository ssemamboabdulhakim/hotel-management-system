from main import Client
import json

while True:
    #get user inputs
    first_name= input("Enter first_name: ").upper()
    last_name= input("Enter last_name: ").upper()
    client_id= input("Enter client_id: ").upper()
    contact= input("Enter contact: ").upper()
    gender= input("Enter gender: ").upper()
    address= input("Enter address: ").upper()
    nationality= input("Enter nationality: ").upper()

    #instance
    client = Client(first_name,last_name,client_id,contact,gender,address,nationality)

    new_client= {
        "first_name": client.first_name,
        "last_name": client.last_name,
        "id": client.client_id,
        "contact": client.contact,
        "gender": client.gender,
        "address": client.address,
        "nationality": client.nationality,
        
    }
    try:
        with open('client.json', "r") as file:
            clients = json.load(file)    
    except (FileNotFoundError,json.JSONDecodeError):
        clients = []


    with open('client.json', "w") as file:
        clients.append(new_client)
        json.dump(clients, file, indent=4)

    
    more_client = input('Do you have more clients? (y/n)').lower()
    if more_client == "y":
        continue
    else:
        break

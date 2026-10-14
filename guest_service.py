from main import Guestservice
import json

while True:
    #get user inputs
    client_id = input("Enter client_id:").upper()
    reservation_id = input("Enter reservation_id:").upper()
    amount = input("Enter amount:").upper()
    client_bill = input("Enter client_bill:").upper()
    current_date = input("Enter current_date:").upper()
    current_time = input("Enter current_time:").upper()
   

     #instance
    clientoffered = Guestservice(client_id,reservation_id,amount,current_date,current_time,)

    new_guest_services= {
        "client_id": clientoffered.client_id,
        "reservation_id": clientoffered.reservation_id,
        "amount": clientoffered.amount,
        "current_date": clientoffered.current_date,
        "current_time": clientoffered.current_time,

     }
    try:
        with open('guest_service.json', "r") as file:
            client_services = json.load(file)
    except (FileNotFoundError,json.JSONDecodeError):
        client_services = []

 
    with open('guest_service.json', "w") as file:
        client_services.append(new_guest_services)
        json.dump(client_services, file, indent=4)

    

    more_guest_services = input('do you want to make more guest_services? (y/n) .upper()').lower()
    if more_guest_services == "y":
        continue
    else:
        break

        




      

    

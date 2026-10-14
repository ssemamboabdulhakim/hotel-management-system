from main import Service
import json

while True:
    #get user inputs
    service_id = input("Enter service_id: ")
    service_name = input("Enter service_name: ")
    service_type = input("Enter service_type: ")
    status = input("Enter status: ")

     #instance
    service =Service(service_id,service_name,service_type,status)

    new_services= {
         
        "service_id": service.service_id,
        "service_name": service.service_name,
        "service_type": service.service_type,
        "status": service.status
        
     }

    try:
        with open('service.json', "r") as file:
            services = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        services = []

    with open('service.json', "w") as file:
        services.append(new_services)
        json.dump(services, file, indent=4)

    more_services = input('do you want to make more services? (y/n)').lower()
    if more_services == "y":
        continue
    else:
        break

        




      

    

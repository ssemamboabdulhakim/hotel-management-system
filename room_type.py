from main import Roomtype
import json

while True:
    #get user inputs
    room_type_id = input("Enter room_type_id: ")
    room_type_name = input("Enter room_type_no: ")
    room_typename = input("Enter room_type_no: ")
    status = input("Enter status: ")

     #instance
    combo = Roomtype(room_type_id,room_type_name,status)

    new_room_types= {
         
        "room_type_id": combo.room_type_id,
        "room_type_name": combo.room_type_no,
        "capacity": combo.capacity

     }
    try:
        with open('room_type.json', "r") as file:
                    room_types = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
         room_types = []   

    with open('room_type.json', "w") as file:
        room_types.append(new_room_types)
        json.dump(room_types, file, indent=4)

    
    more_room_types = input('do you want to know more room_types? (y/n)').lower()
    if more_room_types == "y":
        continue
    else:
        break

        




      

    

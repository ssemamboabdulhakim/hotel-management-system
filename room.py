from main import Room
import json


while True:
    #get user input 
    room_id= input("enter room_id:").upper()
    room_no= input("enter room_no:")
    price_per_nyt= input("enter price_per_nyt:")
    full_day_price= input("enter full_day_price:")
    room_status= input("enter status:")
    # instance
    room = Room(room_id,room_no,price_per_nyt,full_day_price,room_status)
    nights = 10000
    room.calculate_cost(nights)
    days = 20000
    room.compute_fullday_price(days)

    new_room = {
        "room_id": room.room_id,
        "room_no": room.room_no,
        "price_per_nyt":room.price_per_nyt,
        "full_day_price":room.full_day_price,
        "status": room.status,
        
    }

    try:
        with open('room.json', "r") as file:
            room = json.load(file)
    except (FileNotFoundError,json.JSONDecodeError):
        rooms = []    

    
    with open('room.json', "w") as file:
        rooms.append(new_room)
        json.dump(room, file , indent=4)

    more_room = input('do you have more rooms? (yes/no)').lower()
    if more_room == "yes":
        continue
    else:
        break





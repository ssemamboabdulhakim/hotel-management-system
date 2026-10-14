from main import Reservation


import json


while True:
    room_id = input("enter room_id:").upper()
    room_no = input("enter room_no:")
    client = input("enter client:")
    check_in_date = input("enter check_in_date:")
    check_out_date = input("enter check_out_date:")
    check_in_time = input("enter check_in_time:")
    check_out_time = input("enter check_out_time:")

#instances
#reserve rpts the intance of a single paraentcls
    reserve = Reservation(room_id,room_no,client,check_in_date,check_out_date,check_in_time,check_out_time )

    
    new_reservee = {
        "room_id": reserve.room_id,
        "no": reserve.room_no,
        "client": reserve.client,
        "check_in_date": reserve.check_in_date,
        "check_out_date": reserve.check_out_date,
        "check_in_time": reserve.check_in_time,
        "check_out_time": reserve.check_out_time
    }

    try:
        with open('reservation.json', "r") as file:
            reserves = json.load(file)         #reserves rpts the new list being created,
    except (FileNotFoundError,json.JSONDecodeError):
        reserves = []
   
    with open('reservation.json', "w") as file:
        reserves.append(new_reservee)
        json.dump(reserves,file, indent=4)

    more_reservations = input('do you want to make more reservations? (y/n): ')
    if more_reservations == "y":
        continue
    else:
        break

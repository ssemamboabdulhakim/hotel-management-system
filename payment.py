from main import Payment

from datetime import datetime
import json


while True:
    #get user inputs
    payment_id = input("Enter payment_id: .upper()")
    bill_id = input("enter bill id: .upper() ")
    payment_method = input("Enter payment_method: .upper() ")
    current_date = input("Enter current_date:.upper()")
    current_time = input("Enter current_time:.upper()")

     #instance
    payment = Payment(payment_id,bill_id,payment_method,current_date,current_time)

    new_payments= {
         
        "payment_id": payment.payment_id,
        "bill_id": payment.bill_id,
        "payment_method": payment.payment_method,
        "current_date": payment.current_date,
        "curent_time":payment.current_time

     }
    
    try:
        with open('payment.json', "r") as file:
            payments = json.load(file)
    except (FileNotFoundError,json.JSONDecodeError):
        payments =[]     

    
    with open('payment.json', "w") as file:
        payments.append(new_payments)
        json.dump(payments, file, indent=4)


    more_payments = input('do you want to make more payments? (y/n)').lower()
    if more_payments == "y":
        continue
    else:
        break

        




      

    

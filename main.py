class Room:
    def __init__(self,room_no,room_id):
        self.room_id= room_id
        self.room_no= room_no
        self.__price_per_nyt = self.calculate_cost()
        self.__full_day_price = self.compute_fullday_price()
        self.status = None
    
    def __str__(self):
        return f'YOUR ROOM ID:{self.room_id} \n YOUR ROOM NO:{self.room_no} \n YOUR STATUS:{self.status}'    


    def  set_price_pernight (self,value):
        if value < 0:
            raise ValueError('price cannot be negative')
        self.__price_per_nyt = value

    def  get_price_pernight(self):
        return self.__price_per_nyt    

    
    def set_price_pernight (self,value):
        if value < 0:
            raise ValueError('price cannot be negative')
        self.__full_day_price = value 

    def get_full_day_price(self):
        return self.__full_day_price    

    def availability(self):
        return self.status == "available"

    def book_room(self):
        if self.availability ():
            self.status = "booked"
            return True
        return False

    def release_room(self):
       self.status = "available"

    def calculate_cost (self,nights):
        if nights <= 0:
           raise ValueError('nights cant be negative, enter a positive no:.upper()')  
        return nights * self.__price_per_nyt

    def compute_fullday_price(self,days):
        if days <= 0: 
            raise ValueError('days cant be negative, enter a positive no:.upper()')
        return days * self.__full_day_price



class Roomtype:
    PREMIUM_CAPACITY = 8
    ORDINARY_CAPACITY = 4

    
    def __init__(self,room_type_id,room_type_no):
        self.room_type_id= room_type_id
        self.room_type_no= room_type_no
        self.__category = self.set_categoryroom()
        self.__capacity = self.get_capacity()

    def __str__(self):
        return f'YOUR CAT IS:{self.__category} \n YOUR CAPACITY IS:{self.__capacity} '

    def get_categoryroom(self):
        return self.__category
    def set_categoryroom(self, category):
        category = category.lower()
        if category == "premium":
            self.__capacity = Roomtype.PREMIUM_CAPACITY
        elif category == "ordinary":
            self.__capacity = Roomtype.ORDINARY_CAPACITY
        else:
            raise ValueError ('category must be PREMIUM or ORDINARY') 
        self.__category = category

    def get_capacity (self):
        self. __capacity += 1
        return self.__capacity

class Service:

    MENU = {
        "breakfast": 5000,
        "lunch": 10000,
        "supper": 10000,
        "laundry":15000,
        "spa":20000
    }

    STATUSES = ("available", "not_available")

    def __init__(self,service_id,service_name):
        self.service_id= service_id
        self.service_name= service_name
        self.__service_description= Service.MENU 
        self.__unit_cost = self.compute_unit_cost()
        self.status= self.get_status ()

    def __str__ (self):
        return f'SERVICE ID:{self.service_id}\nSERVICE NAME:{self.service_name} \nSERVICE STATUS:{self.status}'         

    def get_service_description(self):
        return self.__service_description
    
    def get_unit_cost(self):
        return self.__unit_cost

    
    def set_unit_cost(self,value):
        if value <= 0:
            raise ValueError('unit cost cannot be negative').upper()
        self.__unit_cost = value
        #keep the description in step with e new price
        self.__service_description = f"{self.service_name} is {value}"

    def check_status (self,value):
        value = str(value).strip().lower()
        if value not in self.Service.STATUSES:
            raise ValueError ('status must be available or not_available').upper()
        return value

    def get_status(self):
        return self.status

    
    def set_status(self,value):
        self.status = self.check_status(value)

    def is_available(self):
        return self.status == "available"    

    def make_available (self):
        self.status = "available"

    def make_unavailable (self):
        self.status = "not_available"    

    def compute_unit_cost(self,quantity):
        if quantity <= 0:
            raise ValueError ('value cant be 0 or negative').upper()
        return quantity * self.__unit_cost

       

class Reservation:
    def __init__(self,reservation_id,room_id,room_no):
        self.reservation_id = reservation_id
        self.room_id= room_id
        self.room_no= room_no
        self.check_in_date= self.set_check_in_date()
        self.check_out_date= self.set_check_out_date()
        self.check_in_time= self.set_check_in_time()
        self.check_out_time= self.set_check_out_time()

    def __str__(self):
        return f'RESERVATION ID:{self.reservation_id} \nCHECK IN DATE:{self.check_in_date} \nCHECK OUT TIME:{self.check_out_time} '    

    def set_check_in_date(self):
        from datetime import datetime
        self.check_in_date = datetime.today().time
        return self.check_in_date
    
    def set_check_out_date(self):
        from datetime import datetime 
        self.check_out_date = datetime.today().date
        return self.check_out_date

    def set_check_in_time(self):
        from datetime import datetime 
        self.check_in_date = datetime.today().time
        return self.check_in_time

    def set_check_out_time(self):
        from datetime import datetime 
        self.check_out_time = datetime.today().time
        return self.__check_out_time

    
    

class Client:
    def __init__(self,first_name,last_name,client_id,contact,gender,address,nationality):
        self.first_name = first_name
        self.last_name = last_name
        self.client_id = client_id
        self.contact = contact
        self.gender = gender
        self.address = address
        self.nationality = nationality
        
    def __str__(self):
        return f'{self.first_name} {self.last_name}\n{self.client_id}\n{self.contact} {self.__nationality}' 
    
class Guestservice:
    def __init__(self,service_id,client_service_id,staff,client_id):
        self.service_id= service_id
        self.client_service_id= client_service_id
        self.client_id= client_id
        self.service_date= self.service_date()
        self.service_time= self.compute_service_time()
        self.__status= self.set_status()
        self.staff= staff
        self.no_of_services= self.get_no_of_services()

    def __str__(self):
        return f'{self.service_id} \n{self.client_id} \n{self.staff}'
    
    def set_service_date(self):
        from datetime import datetime 
        self.service_time =  datetime.today().date
        return self.service_date
    
    def compute_service_time(self):
        from datetime import datetime 
        self.service_time = datetime.today().time
        return self.service_time
    def set_status(self):
        return self.__status
    
    def staff(self):
        return self.staff
    
    def get_no_of_services(self):
        return self.no_of_services
    

class Payment:
    def __init__(self,payment_id,client,payment_method,staff,):
        self.payment_id = payment_id
        self.client = client
        self.payment_method = payment_method
        self.__bill = self.compute_bill
        self.staff = staff

    
    def compute_bill(self):
        return self.__bill

    def get_payment_method(self):
        return self.__payment_method
    
    
    
    


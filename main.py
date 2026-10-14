class Room:
    def __init__(self,room_no,room_id,status,price_per_nyt,full_day_price):
        self.room_id= room_id
        self.room_no= room_no
        self.__price_per_nyt = price_per_nyt
        self.__full_day_price = full_day_price
        self.status = status    
    
    def __str__(self):
        return f'YOUR ROOM ID:{self.room_id} \n YOUR ROOM NO:{self.room_no} \n YOUR STATUS:{self.status}'    

    
    def  get_price_pernight(self):
        return self.__price_per_nyt

    def  set_price_pernight (self,value):
        if value < 0:
            raise ValueError('price cannot be negative')
        self.__price_per_nyt = value

    def get_full_day_price(self):
        return self.__full_day_price
    
    def set_price_pernight (self,value):
        if value < 0:
            raise ValueError('price cannot be negative')
        self.__full_day_price = value 

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
        self.__category = None
        self.__capacity = None

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
        return self.__capacity

    #how many rooms of this type are needed  
    def room_needed(self,guests):
        if guests <= 0:
            raise ValueError ('guests must be greater than 0')
        elif not self.__capacity:
            raise ValueError ('category and capacity must be set first')

    


class Service:

    MENU = {
        "breakfast": 5000,
        "lunch": 10000,
        "supper": 10000,
        "laundry":15000,
        "spa":20000
    }

    STATUSES = ("available", "not_available")

    def __init__(self,service_id,service_name,status):
        self.service_id= service_id
        self.service_name= service_name
        self.__service_description= Service.STATUSES
        self.__unit_cost = Service.MENU 
        self.status= status 

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
        self.__check_in_date= "12/10/2026"
        self.__check_out_date= "13/10/2026"
        self.__check_in_time= "12:00"
        self.__check_out_time= "15:00" 

    def __str__(self):
        return f'RESERVATION ID:{self.reservation_id} \nCHECK IN DATE:{self.check_in_date} \nCHECK OUT TIME:{self.check_out_time} '    
        
    def reservation_id(self):
        return self.reservation_id

    def check_in_date(self):
        return self.__check_in_date
    def set_check_in_date(self, value):
        self.__check_in_date = value

    def check_out_date(self):
        return self.__check_out_date

    def set_check_out_date(self,value):
        self.__check_out_date = value

    def check_in_time(self):
        return self.__check_in_time

    def set_check_in_time(self,value):
        self.__check_in_time = value

    def check_out_time(self):
        return self.__check_out_time

    def set_check_out_time(self,value):
        self.__check_out_time = value
    
    

class Client:
    def __init__(self,first_name,last_name,contact,gender,address):
        self.first_name= first_name
        self.last_name= last_name
        self.__client_id= "c001"
        self.contact= contact
        self.gender = gender
        self.address = address
        self.__nationality = "ugandan"
        
    def __str__(self):
        return f'{self.first_name} {self.last_name}\n{self.client_id}\n{self.contact} {self.__nationality} '

    def set_client_id(self):
        return self.__client_id
    
    def get_nationality(self):
        return self.__nationality
    

class Payment:
    def __init__(self,payment_id,client,staff):
        self.payment_id = payment_id
        self.cleint = Client
        self.__payment_method = "none"
        self.__staff = staff

    
    def set_payment_method(self):
        return self.__payment_method

    def get_payment_method(self):
        return self.__payment_method
    def set_staff(self):
        return self.__staff
    def get_staff(self):
        return self.__staff
    
    



#adding a comment     

class Guestservice:
    def __init__(self,service_id,client_service_id,service_date,service_time,staff,guest_id):
        self.__service_id= service_id
        self.client_service_id= client_service_id
        self.guest_id= guest_id
        self.service_date= service_date
        self.service_time= self.compute_service_time()
        self.__status= None
        self.__staff= staff
        self.__no_of_services= 0

    def __str__(self):
        return f'{self.__service_id} \n{self.}'
    
    def guest_service_id(self):
        return self.guest_service_id
    def guest_id(self):
        return self.guest_id
    def service_date(self):
        from datetime import datetime 
        self.service_time =  datetime


        return self.service_date
    def compute_service_time(self):
        from datetime import datetime 
        self.service_time = datetime.today().time
        return self.service_time
    def status(self):
        return self.status
    def staff(self):
        return self.staff
    def no_of_services(self):
        return self.no_of_services

        


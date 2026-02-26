# isinstance(object, Class) 
# checks if an object is an instance of a class
# or any of its parent classes (it considers inheritance)

class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def make_call(self):
        return f"{self.brand} {self.model} is making a call."

    def full_name(self):
        return f"{self.brand} {self.model} - ${self.price}"
    

# children class inheritance
class SmartPhone(Phone):
    def __init__(self, brand, model, price, ram, internal_memory, rear_camera):
        super().__init__(brand, model, price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

    def take_photo(self):
        return f"{self.brand} {self.model} is taking a photo with {self.rear_camera} MP camera."
   
   
   

class FlagShip(SmartPhone):
    def __init__(self, brand, model, price, ram, internal_memory, rear_camera, front_camera):
        super().__init__(brand, model, price, ram, internal_memory, rear_camera)
        self.front_camera = front_camera
        

phone1 = Phone('xiaomi', 'redmi', 7000000)

iphone = SmartPhone('Iphone', '15 pro', 12000000, '8GB', '256GB', '25MP')

onePlus = FlagShip('samsung', 'A7', 15000000, '8GB', '512GB', '25MP', '12MP')
# print(onePlus.__dict__)


# object phone1
print(isinstance(phone1, Phone)) # True, because phone1 is created directly from the Phone class

# object iphone
print(isinstance(iphone, Phone)) # True,  iphone is a SmartPhone, which inherits from Phone
print(isinstance(iphone, SmartPhone)) # True,  iphone is directly a SmartPhone object

# object OnePlus
print(isinstance(onePlus, Phone))  # True, onePlus is a FlagShip, which inherits from SmartPhone, which inherits from Phone
print(isinstance(onePlus, SmartPhone))# True, onePlus is a FlagShip (subclass of SmartPhone)
print(isinstance(onePlus, FlagShip)) # True,  onePlus is directly a FlagShip object


# ‼️
print(isinstance(phone1, FlagShip)) # False,  phone1 is just a Phone, not a FlagShip or any of its subclasses



        
    
        
    
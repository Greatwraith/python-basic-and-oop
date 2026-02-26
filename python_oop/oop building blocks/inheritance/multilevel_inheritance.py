# MULTILEVEL INHERITANCE
# is when a class inherits from another class,
# and that class inherits from another class

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
   
   
   
# ‼️‼️‼️✅‼️‼️‼️
# MULTILEVEL INHERITANCE
# FlagShip is a child class of SmartPhone and inherits its attributes and methods
class FlagShip(SmartPhone):
    def __init__(self, brand, model, price, ram, internal_memory, rear_camera, front_camera):
        super().__init__(brand, model, price, ram, internal_memory, rear_camera)
        self.front_camera = front_camera
        

onePlus = FlagShip('samsung', 'A7', 15000000, '8GB', '512GB', '25MP', '12MP')
print(onePlus.__dict__)

# even though full_name() method is not defined in FlagShip,
# it still works because FlagShip inherits(methods and attributes) it from Phone
print(onePlus.full_name())    # from Phone
print(onePlus.make_call())    # from Phone
print(onePlus.take_photo())   # from SmartPhone
        
    
        
    
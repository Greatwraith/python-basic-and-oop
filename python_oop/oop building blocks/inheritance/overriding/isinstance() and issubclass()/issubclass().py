# issubclass()
# issubclass(Class1, Class2) → checks if Class1 is a child/subclass of Class2.

# Returns True if Class1 inherits from Class2
# Returns False if it doesn’t

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


# ..?
print(issubclass(FlagShip, SmartPhone))  # True, FlagShip is a child of SmartPhone
print(issubclass(SmartPhone, Phone)) # True, SmartPhone is a child of Phone
print(issubclass(FlagShip, Phone))
# True, FlagShip is a children of SmartPhone
# then
# a SmartPhone is a children of Phone




        
    
        
    
# PARENT CLASS / BASE CLASS
class Phone: 
    def __init__(self, type, brand, model, price):
        self.type = type
        self.brand = brand
        self.model = model
        self.price = max(0, price)
    
    @staticmethod
    def call_number(phone_number):
        print (f'calling {phone_number}...')
       
    def full_name(self):
        return f'{self.brand} {self.model} {self.type}'
        

# CHILDREN CLASS OF THE PARENT CLASS / DERIVED CLASS
class FullSpec(Phone): # FullSpec inherits everything(attributes or method) that are in the Phone(parent class)
    def __init__(self, type, brand, model, price, ram, internal_memory):
        
        # calling parent class's(Phone) Constructor
        super().__init__(type,brand, model, price) 
        
        # New Attributes for FullSpec
        self.ram = ram
        self.internal_memory = internal_memory
    
    # memakai atribut hasil inheritance parent class(Phone)
    # ditambah atribut baru milik child
    def specification(self):
        return f'{self.brand} {self.model} {self.type} | Rp{self.price} | spec: {self.ram} Ram with {self.internal_memory} internal memory'
        
    # Method disebut override kalau ....
    # NAMA method di child SAMAdengan method di parent class.
    # 
    # def specification(self):
    #          return ....
        
        
        
# call object which is using class Phone
phone1 = Phone('Smartphone','Iphone', 15, 12000000)
print(phone1.__dict__)


# call object which is using class FullSpec
laptop1 = FullSpec('Laptop', 'Apple','macbook m1',12000000, '8GB', '256GB')
print(laptop1.__dict__)

print(laptop1.specification())







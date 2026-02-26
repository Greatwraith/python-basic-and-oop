# Encapsulation 
# menggabungkan data dan methods ke dalam sebuah kelas dan mengontrol bagaimana data tersebut diakses dan dimodifikasi.

class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.__price = max(0, price)
    
    @staticmethod
    def call_number(phone_number):
        print (f'calling {phone_number}...')
       
    # Encapsulation too 
    # Uses internal data then Formats it for the user
    # format {self.brand} {self.model}
    def full_name(self):
        return f'{self.brand} {self.model}'
        
    def get_price(self):
        return self.__price
        
        
phone1 = Phone('Iphone', 15, 12000000)
print(phone1.__dict__)
print(phone1.full_name())
phone1.call_number('0800400500')
print(phone1.get_price())



# You are encapsulating: brand, model, price(these 3 are related data)
# using self.xxxx inside one object (Phone)
# 
# instead of :
# brand = "Iphone"
# model = 15
# price = 12000000

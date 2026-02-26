class Product:
    def __init__(self, type, name, brand, model, price):
        self.type = type 
        self.name = name
        self.brand = brand
        self.model = model
        self.price = price
        self.nameAndModel = brand + " " + name + " " + model
        
# 1st PRODUCT
a_laptop = Product('Laptop', 'Macbook', 'Apple', 'm1', 8000000)

print(a_laptop.type)
print(a_laptop.name) 
print(a_laptop.brand)
print(a_laptop.model)
print(a_laptop.price)
print(a_laptop.nameAndModel)



print(" ")

# 2nd PRODUCT

an_iphone = Product('Phone', 'Iphone', 'Apple', '15 pro max', 8000000)

print(an_iphone.type)
print(an_iphone.name)
print(an_iphone.brand)
print(an_iphone.model)
print(an_iphone.price)
print(an_iphone.nameAndModel)

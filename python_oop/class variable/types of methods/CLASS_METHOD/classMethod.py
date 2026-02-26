class Laptop:   # Class
    discount = 10  #Class Variable
    
    def __init__(self, name,price):
        self.name = name   # Class Attribues
        self.price = price
        
    @classmethod  #Class Method
    #  from_string > receive the string
    # "my laptop is macbook and price is 500000"
    def from_string(clr, string):
        import re
        
        # Extract values using regex
        # from  "my laptop is macbook and price is 500000"
        # will find ['is macbook', 'is 500000']
        item = re.findall(r'is \w*', string)
        
        # Clean the data of ['is macbook', 'is 500000']
        name = item[0][3:] # macbook
        price = item[1][3:] # 500000
        
        # Call the class (clr == Laptop), which runs __init__
        # Creates a Laptop object and returns it
        return clr(name, int(price))
        
        
    def ApplyDiscount(self):  #instance Method
        discountValue = (self.price/100)*self.discount
        priceDiscount = self.price - discountValue
        return int(priceDiscount)
        
# Create a Laptop object using the class method
# from_string() parses the sentence, calls the constructor,
# and returns a fully built Laptop object
laptop1 = Laptop.from_string('my laptop is macbook and price is 500000')


  
# Print, that Shows that the object was created successfully
# Output: {'name': 'macbook', 'price': 500000}
print(laptop1.__dict__)


# Call the instance method ApplyDiscount()
# ‼️✅‼️ Python AUTOMATICALLY passes laptop1 as 'self'
# Uses the class variable discount (10%)
print(laptop1.ApplyDiscount())


# Override the class variable 'discount' for this instance only
# This creates an instance variable named 'discount'
laptop1.discount = 5


# Print the instance dictionary again
# Now includes 'discount' because it was added to the instance
# Output: {'name': 'macbook', 'price': 500000, 'discount': 5}
print(laptop1.__dict__)


# Call ApplyDiscount() again
# This time it uses the instance discount (5%) instead of class discount
print(laptop1.ApplyDiscount())





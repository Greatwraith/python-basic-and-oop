class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        
        # Price must never be negative
        self.price = max(price, 0) # Ensure price is not negative

    
    @property # lets you access a method like an attribute.
    def complete_specification(self):
        return f"{self.brand} {self.model_name}, Price: {self.price}"

    # UPDATED PRICE, ensuring it's not negative
    def update_price(self, new_price):
        self.price = max(new_price, 0)  

# Try to set a negative price
phone1 = Phone("Nokia", "1100", -5000)  # Negative will be 0
print(phone1.complete_specification)  #  Price: 0

# Trying to set a negative price again
phone1.update_price(-7000)  
print(phone1.complete_specification)  # Price: 0

# a valid price
phone1.update_price(2000)  
print(phone1.complete_specification)  # Output Price: 2000




# @property
# phone1.complete_specification
# to make u able to  call a method behind the scenes, without parentheses.

# ✅ THIS ‼️
# self.price = max(price, 0)

# ✅ IS AS THE SAME AS ‼️
# if price < 0:
#     self.price = 0
# else:
#     self.price = price
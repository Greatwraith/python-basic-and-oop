# WHY THIS IS CALLED: Object Techniques + Class Variable
#  
# KEY POINT : CUSTOMIZING ONE OF ITS CLASS VARIABLE
# Class variable (shared default for all Wallet objects)
# 
#
# 1. Class Variable:
#    `discount` is defined at the CLASS level.
#    This means ALL Wallet objects share the same default discount (10%).
#
# 2. Object Techniques:
#    Each Wallet object can:
#    - Have its OWN attributes (e.g. wallet1.leather)
#    - Override class variables (e.g. wallet1.discount = 0)
#
# 3. Key Concept:
#    Python looks for attributes in this order:
#    1) Object (instance)
#    2) Class
#    So when `wallet1.discount = 0` is set,
#    the object overrides the class variable ONLY for itself.


class Wallet:
    # Class variable (shared default for all Wallet objects)
    discount = 10

    def __init__(self, name, price):
        # Instance variables (unique per object)
        self.name = name
        self.price = price
    
    def ApplyDiscount(self):
        # Uses object discount first, then class discount if object doesn't have one
        discount_amount = (self.price / 100) * self.discount
        priceWithDiscount = self.price - discount_amount
        return priceWithDiscount


# Creating an object (instance)
wallet1 = Wallet('Eiger', 550000)
wallet1.leather = "sintetis"
print(wallet1.__dict__)

# Uses class variable discount (10%)
print(wallet1.ApplyDiscount())

# Object technique: customize or override class variable for this object only
wallet1.discount = 0

# Now uses object-level discount, not class-level
print(wallet1.ApplyDiscount())
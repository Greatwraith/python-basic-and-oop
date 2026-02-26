# the topic is naming convention

class Wallet:
    def __init__(self, name, brand, price):
        # public attribute: can be accessed and modified freely
        self.name = name          
        self.brand = brand        
        self.price = price        

        self._discount = 5 
        # single underscore (_) means "this attribute is intended for internal use"
                                 
         # it is NOT truly private, only private by convention.
         # its function is just to tell other developers/coder who use this code not to change the value of it.
        #  it doesn't really work like private in PHP oop

    # public method that uses the "private-by-convention" attribute
    def apply_discount(self):
        discounted = (self.price / 100) * self._discount
        final_price = self.price - discounted
        return final_price


wallet1 = Wallet('wallet', 'prada', 8000000)

# calling the method normally (uses the internal _discount value = 5)
print(wallet1.apply_discount())

# even though _discount is intended to be private,
# Python does NOT prevent us from accessing or changing it
# this works because Python treats everything as public
wallet1._discount = 2

# the result changes because the value of _discount was modified
print(wallet1.apply_discount())
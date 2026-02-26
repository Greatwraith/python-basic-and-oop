# Creating an instance of a class

class Apple:
    def __init__(self):
        self.name = "apple"
        self.color = "red"
        self.edible = True
        self.flavor = "sweet"

turkish_tea = Apple()
print("the turkish tea is made of {} and taste {} ".format(turkish_tea.name, turkish_tea.flavor))  
        
        
        
        
# When writing a Python class, you define a method called __init__ to be your constructor.
# the first constructor must always be self.
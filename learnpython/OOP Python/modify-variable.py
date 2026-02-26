# MODIFYING THE VALUE OF A VARIABLE
class Apple:
    def __init__(self, color, flavor, origin):
        self.name = "apple"
        self.color = color
        self.flavor = flavor
        self.origin = origin

fuji = Apple("red", "sweet", "Japan")
turkish_tea = Apple("reddish black", "bitter", "Turkey")

print("the fuji {} is {} and taste {} ".format(fuji.name, fuji.color, fuji.flavor))
print("the turkish tea is made of: {} ,  taste : {}, it looks: {} , it is from: {}".format(turkish_tea.name, turkish_tea.flavor, turkish_tea.color, turkish_tea.origin))

# we can change the value of a variable by using the dot notation and assigning a new value to it.




print("     ")






# STR is a special method that is used to
# define how an object should be represented as a string.
class Saffron:
    def __init__(self, type, color, flavor, origin):
        self.name = "saffron"
        self.type = type
        self.color = color
        self.flavor = flavor
        self.origin = origin
    
    def __str__(self):
        return "The {} is a type of {} that is {} in color, has a {} flavor, and originates from {}.".format(self.name, self.type, self.color, self.flavor, self.origin)
    
saffron = Saffron("spice", "red", "bitter", "Iran")
print(saffron)
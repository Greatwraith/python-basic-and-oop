# a method is a function that is defined inside a class 
# is used to perform a specific action on an object of that class.

class Cow:
    def speak(self):
        name = "cow"
        print("Moo! Moo!  im a cow my name is {}  Moo! Moo!".format(self.name))
        
a_cow = Cow()
a_cow.name = "Petunia"
a_cow.speak()



# i think he's alone, let's give him a friend and see if they can speak together.

jared = Cow()
jared.name = "Jared"
jared.speak()




# We've now created two instances of the Cow class each of them with their own name. 
# When calling this speak method each of them prints their name and not the other.

# Variables that have different values for different instances of the same class are called instance variables
# just like the name variable in this example.
# Since methods are just functions that belong to a specific class, they can work as any other function. 


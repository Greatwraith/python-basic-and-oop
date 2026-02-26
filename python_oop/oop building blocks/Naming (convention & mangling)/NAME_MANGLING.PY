class RemoteControlArdhan:
    def __init__(self, type, model, price):
        self.type = type
        self.model = model
        self.price = price
        
    def __printSpec(self):
        print("TYPE: {} \n\tMODEL: {} \n\tPRICE: {}".format(self.type, self.model, self.price))
        
        
        
class RemoteControlJonathan(RemoteControlArdhan):
    def __init__(self, type, model, price):
        self.type = type
        self.model = model
        self.price = price
        
    def __printSpec(self):
        print("TYPE: {} \n\tMODEL: {} \n\tPRICE: {}".format(self.type, self.model, self.price))
        
ardhanRC = RemoteControlArdhan('Airplane RC', 'Fighter Jet', 6200000 )
jonathanRC = RemoteControlJonathan('Truck RC', 'Cargo Truck', 4500000)




print(ardhanRC._RemoteControlArdhan__printSpec())


print(jonathanRC._RemoteControlJonathan__printSpec())
# both of them have the same method which is princtSpec
# to print the printSpec(a method) who belongs to class RemoteControlJonathan :
# _RemoteControlJonathan__printSpec()
# _theClassName__theMethodOfTheClassName



# since we use name mangling (__printSpec),
# its's avoid name conflicts between parent and child classes
# that have methods with the same name

# the method is called based on the class that owns the method
# using the format:
# _theClassName__theMethodName

# _theClassName        → the class that owns the method
# __theMethodName      → the original method name (with double underscore)


    
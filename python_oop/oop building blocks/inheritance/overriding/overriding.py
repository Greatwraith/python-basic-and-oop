# BASE CLASS (Parent)
class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def showInfo(self):  # METHOD showInfo() in parent class Hero
        print("showInfo di class Hero\n\tName: {}\n\tHealth: {}".format(
            self.name,
            self.health
        ))

# CHILD CLASS (Overrides showInfo)
class Hero_intelligent(Hero):
    def __init__(self, name):
        super().__init__(name, 100)  # call parent constructor and set health = 100

    # METHOD OVERRIDING
    def showInfo(self):
        print("showInfo di subclass Hero_intelligent\n\tName: {}\n\tTipe: intelligent\n\tHealth: {}".format(
            self.name,
            self.health
        ))

# CHILD CLASS to show hero's strength (Does NOT override showInfo)
class Hero_strength(Hero):
    def __init__(self, name):
        super().__init__(name, 200) # call parent constructor and set health = 200

    # Override showInfo to show type strength
    def showInfo(self):
        print("showInfo di subclass Hero_strength\n\tName: {}\n\tTipe: strength\n\tHealth: {}".format(
            self.name,
            self.health
        ))
# OBJECTS
lina = Hero_intelligent("lina")
axe = Hero_strength("axe")

# CALL METHODS
lina.showInfo()   # uses overridden method (Hero_intelligent)
axe.showInfo()    # uses overridden method (Hero_strength)

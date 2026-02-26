# BASE CLASS
class Hero:
    def __init__(self, name, intelligent_type, skill, health):
        self.name = name
        self.intelligent_type = intelligent_type
        self.skill = skill
        self.health = health
        
    def showInformation(self):
        print("show information from class Hero")
        print("{} | Health: {}".format(self.name, self.health))


# CHILD CLASS (Intelligent-based Hero)
class Hero_intelligent(Hero):
    def __init__(self, name, intelligent_type, skill, health, special_intelligent):
        super().__init__(name, intelligent_type, skill, health)  # Call base class constructor
        self.special_intelligent = special_intelligent
        
    # METHOD OVERRIDING
    def showInformation(self):
        print("show information from class Hero_intelligent")
        print(
            "Name: {}\n\tHealth: {}\n\tIntelligent Type: {}".format(
                self.name, self.health, self.intelligent_type
            )
        )
        print("Your hero special intelligent type: {}".format(self.special_intelligent))


# CHILD CLASS (Skill-based Hero)
class Hero_skill(Hero_intelligent):
    def __init__(self, name, intelligent_type, skill, health, special_intelligent, skill_type):
        super().__init__(name, intelligent_type, skill, health, special_intelligent)
        self.skill_type = skill_type
        
    # METHOD OVERRIDING
    def showInformation(self):
        print("show information from class Hero_skill")
        print(
            "Name: {}\n\tHealth: {}\n\tIntelligent Type: {}\n\tSpecial Intelligent: {}\n\tSkill Type: {}\n\tSkill Value: {}".format(
                self.name, self.health, self.intelligent_type, self.special_intelligent, self.skill_type, self.skill
            )
        )
        
# Base hero
axe = Hero("Axe", intelligent_type="Balanced", skill=50, health=100)
axe.showInformation()

print("\n")

# Intelligent hero
mage = Hero_intelligent("Mage", intelligent_type="Magic", skill=40, health=80, special_intelligent=95)
mage.showInformation()

print("\n")

# Skill hero
warrior = Hero_skill(
    "Warrior", 
    intelligent_type="Strength", 
    skill=90, 
    health=120, 
    special_intelligent=85, 
    skill_type="Swordsmanship"
)
warrior.showInformation()
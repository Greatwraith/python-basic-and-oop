class Member:
    status = 'active' 
    description = 'is a member' 
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # Mengambil nilai default dari class variable di atas
        self.status = Member.status
        self.description = Member.description
        
    @classmethod
    def take_string(clr, string):
        import re
        memberName = re.findall(r'named \w+ \w+', string)
        memberAge = re.findall(r'is \d+', string)
        
        # Clean the extracted data
        name = memberName[0][6:]   # remove "named "
        age = memberAge[0][3:]     # remove "is "
        return clr(name, int(age)) # Build & return the object
        
    def welcome(self):
        return f"welcometo the Northeast gym {self.name} your status is {self.status} and {self.description}"
        
        
# Membuat object member
member1 = Member.take_string(
    "a member named john doe is detected as an active member age is 21"
)

# Menampilkan pesan sambutan
print(member1.welcome())


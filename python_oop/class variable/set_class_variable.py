class Member:
    # STATUS & DESCRIPTION member yang masuk akan secara default 
    # di set ke 'aktif' dan 'adalah member'
    
    # Nilai default untuk semua member
    status = 'active' # class variable 'status'
    description = 'is a member' # class variable 'desription'
    
    def __init__(self, name, age):
        # Instance variables (milik tiap object)
        self.name = name
        self.age = age
        
        # Mengambil nilai default dari class variable di atas
        self.status = Member.status
        self.description = Member.description
        
    def welcome(self):
        return f"welcometo the Northeast gym {self.name} your status is {self.status} and {self.description}"
        
        
# Membuat object member
member1 = Member('John doe', 17)

# Menampilkan pesan sambutan
print(member1.welcome())

# Menampilkan status dan deskripsi default member
print(member1.status)
print(f"and {member1.description}")
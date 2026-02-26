# Encapsulation = mengunci data (PIN & kunci mesin)
# Abstraction   = fungsi yang boleh dipakai user (tombol ATM)

class Hero:
    
    def __init__(self, name, health, attackPower):
        # PRIVATE data (tidak boleh diakses langsung)
        self.__name = name
        self.__health = health
        self.__attackPower = attackPower
    
    # getter yang READ-ONLY access (ABSTRACTION)
    def getName(self):
        return self.__name
        
    def getHealth(self):
        return self.__health
        
    # setter yang controlled behavior (ABSTRACTION)
    def diserangMusuh(self, powerSerangan):
        self.__health -= powerSerangan
        
    def ubahAttackPower(self, updatedAttackPower):
        self.__attackPower = updatedAttackPower
        
        
# =========================
# GAME SIMULATION
# =========================

lancelot = Hero('lancelot', 100, 70)

# User bisa MELIHAT data
print(lancelot.getName())
print(lancelot.getHealth())

# User TIDAK boleh mengubah data langsung (ENCAPSULATION)
# lancelot.__health = -1  # ❌

# User mengubah data lewat method resmi (ABSTRACTION)
lancelot.diserangMusuh(20)
lancelot.ubahAttackPower(100)

print(lancelot.getHealth())



# karena adanya encapsulation yg melindungi data, user tidak bisa mengubah data secara langsung,
# tetapi harus lewat abstraction yaitu method yang sudah ditentukan.

# user bisa :
#     - melihat data.  
#     - mengubah data melalui cara resmi, yaitu method yang sudah ditentukan
#     - tidak bisa mengubah data secara langsung karena adanya encapsulation (encapsulation melindungi data dari akses langsung)
#     - menggunakan abstraction, yaitu fungsi-fungsi yang disediakan dan diperbolehkan untuk digunakan tanpa perlu mengetahui detail implementasi di baliknya (abstraction menyembunyikan detail implementasi)
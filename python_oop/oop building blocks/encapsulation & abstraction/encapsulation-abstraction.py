# Encapsulation ibarat PIN & kunci mesin
# Abstraction ibarat fungsi yang diperbolehkan dan bisa digunakanan user 

# =========================
# ENCAPSULATION (OOP) |Encapsulation itu seperti gerbang keamanan
# =========================
# Encapsulation adalah konsep OOP untuk:
# 1. Menggabungkan data (attributes) dan behavior (methods) ke dalam satu class
# 2. Melindungi data penting agar tidak bisa diubah secara langsung dari luar class
# 3. Mengontrol bagaimana data diakses dan dimodifikasi melalui method tertentu

# Analogi sederhana:
# Bayangkan ATM:
# ❌ Kamu tidak bisa membuka mesin dan mengambil uang langsung
# ✅ Kamu hanya bisa menarik uang lewat tombol dan PIN
# Uangnya bisa berubah, tapi CARANYA dikontrol

class Hero:
    
    def __init__(self, name, health, attackPower):
        # Attribute dengan awalan __ bersifat PRIVATE
        # Artinya: tidak boleh diakses atau diubah langsung dari luar class
        self.__name = name
        self.__health = health
        self.__attackPower = attackPower
    
    # =========================
    # GETTER (READ-ONLY ACCESS)
    # =========================
    # Getter berfungsi untuk:
    # - Memberikan akses baca ke data private
    # - Tanpa memberi izin untuk mengubah data secara langsung
    
    def getName(self):
        return self.__name
        
    def getHealth(self):
        # ABSTRACTION:
        # User cukup tahu "ambil health"
        # Tidak perlu tahu health disimpan sebagai apa dan di mana
        return self.__health
        
    # =========================
    # SETTER / BEHAVIOR
    # =========================
    # Perubahan data TIDAK dilakukan secara langsung,
    # tetapi lewat method yang sudah ditentukan (aturan game)
    
    def diserangMusuh(self, powerSerangan): # Mengurangi health saat hero diserang musuh
        # ABSTRACTION:
        # User hanya tahu "hero diserang"
        # User tidak perlu tahu bagaimana health dihitung atau disimpan      
        self.__health -= powerSerangan
        
    def ubahAttackPower(self, updatedAttackPower): # Mengubah attack power melalui method resmi
        # ABSTRACTION:
        # User cukup tahu "ambil health"
        # User Tidak perlu tahu health disimpan sebagai apa dan di mana    
        self.__attackPower = updatedAttackPower
        
        
# =========================
# GAME SIMULATION
# =========================

# Awal game: setingan default hero
lancelot = Hero('lancelot', 100, 70)

# Game berjalan
# User BISA melihat status hero
print(lancelot.getName())
print(lancelot.getHealth())

# User TIDAK BOLEH mengubah data secara langsung
# Baris di bawah ini TIDAK mengubah data asli karena attribute bersifat private
# Python hanya akan membuat attribute BARU, bukan mengganti yang asli

# lancelot.__name = "Alucard"
# lancelot.__health = -1
# print(lancelot.getName())
# print(lancelot.getHealth())

# Ini juga SALAH:
# getName dan getHealth adalah METHOD, bukan variable
# Menimpanya akan merusak behavior object

# lancelot.getName = "Miya"
# lancelot.getHealth = 20
# print(lancelot.getName())  # TypeError


# ABSTRACTION (OOP) | # Perubahan data yang BENAR (lewat aturan game) | diperbolehkan untuk diubah
lancelot.diserangMusuh(20)
lancelot.ubahAttackPower(100)
print(lancelot.getHealth()) # Health berubah secara terkontrol




# =========================
# ABSTRACTION (OOP)
# =========================
# Abstraction adalah konsep OOP untuk:
# 1. Menyembunyikan detail implementasi yang tidak perlu diketahui user
# 2. Menampilkan fungsi yang penting saja (interface sederhana)
# 3. Membuat object mudah digunakan tanpa perlu tahu cara kerjanya

# Dalam kode ini:
# User TIDAK perlu tahu:
# - bagaimana health disimpan (__health)
# - bagaimana health dikurangi
# - bagaimana attackPower diubah
#
# User HANYA perlu tahu:
# - hero bisa diserang
# - hero punya health
# - hero punya attack power
#
# Inilah yang disebut abstraction
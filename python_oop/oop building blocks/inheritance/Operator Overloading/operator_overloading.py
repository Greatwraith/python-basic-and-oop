# OPERATOR OVERLOADING
# Operator overloading = memberi arti khusus pada operator (+, -, *) biasanya menggunakan method khusus.
# menggunakan method khusus (__add__, __sub__, __mul__) yang otomatis dipanggil
# saat operator tersebut digunakan pada OBJECT dari sebuah class

class Vehicle:
    def __init__(self, brand, model, year, price):
        # constructor: menyimpan data kendaraan
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        
    # __add__ dipanggil otomatis saat object + object
    # contoh: carIWant + motorbikeIWant
    def __add__(self, other):
        return self.price + other.price # # yang dijumlahkan adalah price dari kedua object
        
    # __sub__ dipanggil otomatis saat object - object
    def __sub__(self, other):
        return self.price - other.price
        
    # __mul__ dipanggil otomatis saat object * object
    def __mul__(self, other):
        return self.price * other.price
        
        
# membuat object Vehicle
carIWant = Vehicle('Lexus', 'LX 700H', '2025', 232000)
print(carIWant.__dict__)  # menampilkan isi attribute object dalam bentuk dictionary

motorbikeIWant = Vehicle('Harley Davidson', 'roadglide', '2010', 150000)
print(motorbikeIWant.__dict__)

#  ‼️ ⬇️PENTING DI PAHAM⬇️I ‼️
# di sini operator +, -, * TIDAK bekerja seperti angka biasa
# tapi memanggil method __add__, __sub__, __mul__ yang kita buat
totalHarga = carIWant + motorbikeIWant # memanggil dan menjalankan method AddPrice
selisihHarga = carIWant - motorbikeIWant #  memanggil dan menjalankan method SubPrice
perkalianHarga = carIWant * motorbikeIWant #  memanggil dan menjalankan method SubPrice



# BISA JUGA DENGAN CARA INI!!!
# selisihHarga = carIWant.__sub__(motorbikeIWant)
# perkalianHarga = carIWant.__mul__(motorbikeIWant)
# totalHarga = carIWant.__add__(motorbikeIWant)

# ⬇️ JADI ADA DUA CARA MEMANGGIL OPERATOR OVERLOADING ⬇️
# carIWant + motorbikeIWant
# bisa juga: ⬇️
# carIWant.__sub__(motorbikeIWant)
# NOTE : sama saja hanya beda penulisan

print(f'total Harga: {totalHarga}')
print(f'selisih Harga: {selisihHarga}')
print(f'perkalia nHarga: {perkalianHarga}')
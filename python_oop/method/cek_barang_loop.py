class Barang:
    def __init__(self, nama, status):
        self.nama = nama
        self.status = status
        
        
    def result(self):
        if self.status == 'baru':
            return 'bagus'
        elif self.status == 'bekas':
            return 'layak'
        else:
            return 'rusak'
            

b1 = Barang('Laptop', 'baru')
b2 = Barang('Sparepart otomotif', 'bekas')
b3 = Barang('ban', 'bekas')
b4 = Barang('speaker', 'rusak')

objek_barang = [b1, b2, b3, b4]

barangBagus = []
barangLayak = []
barangRusak = []

statusBarang = {}

for barang in objek_barang:
    if barang.result() == 'bagus':
        barangBagus.append(barang.nama)
        statusBarang['ini barang yang bagus: '] = barangBagus
    elif barang.result() == 'layak':
        barangLayak.append(barang.nama)
        statusBarang['ini barang bekas yang layak: '] = barangLayak
    else:
        barangRusak.append(barang.nama)
        statusBarang['ini barang RUSAK: '] = barangRusak
        
print(statusBarang)



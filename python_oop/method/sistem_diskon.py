class Produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga
    
    def diskon(self,nilaiDiskon):
        jumlahDiskon = (self.harga/100) * nilaiDiskon
        harga_diskon = self.harga - jumlahDiskon
        return int(harga_diskon)
   
produkSatu = Produk('mesin cuci', 3500000)
produkDua = Produk('kulkas', 5200000 )
produkTiga = Produk('Tv', 3000000)
# print(produkSatu.diskon(10))

produk_objek = [produkSatu, produkDua, produkTiga]

produkTersusun = []
semuaProduk = {}


for produk in produk_objek:
    produkTersusun.append({
        'nama':produk.nama,
        'harga_awal':produk.harga,
        'harga setelah diskon':produk.diskon(10)
    })
    semuaProduk = {
        'ini semua produk setelah diskon':produkTersusun
    }
    
print(semuaProduk)


        
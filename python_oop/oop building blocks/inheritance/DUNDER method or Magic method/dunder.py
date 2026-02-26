# Dunder method / Magic method

# __str__ : untuk menampilkan informasi yang user-friendly (untuk di tampilkan PELANGGAN)
# tinggal print(object) saja, maka Python akan otomatis memanggil __str__ method(informasi untuk user)

# __repr__ : untuk menampilkan informasi untuk programmer (untuk di tampilkan PROGRAMMER)
# biasa nya informasi nya adalah lebih info/spesifikasi detail & struktur object.

# tinggal print(repr(object)) saja, maka Python akan otomatis memanggil __repr__


class Furniture:
    def __init__(self, name, brand, made_of, price):
        self.name = name
        self.brand = brand
        self.made_of = made_of
        self.price = price
        
    # untuk menampilkan ke pelanggan
    def __str__(self):
        return "NAME: {} \n\tBRAND: {} \n\tMADE OF: {} \n\tPRICE: {}".format(
            self.name, self.brand, self.made_of, self.price
        )

    # untuk programmer (struktur + isi object)
    def __repr__(self):
        return (
            "CLASS NAME: Furniture\n"
            "\tCONTAINS: furniture(name'str', brand'str', made_of'str', price:INTEGER \n\t"
            "CLASS NAME: Furniture\n"
            "\tCONTAINS: Furniture("
            "name='str', brand='str', made_of='str', price=int"
            ")\n"
            "\tOBJECT DATA: "
            "Furniture(name={!r}, brand={!r}, made_of={!r}, price={!r})"
        ).format(
            self.name,
            self.brand,
            self.made_of,
            self.price
        )
        
myCouch = Furniture(
    'Livingroom Couch',
    'Ikea',
    'strong wood and premium Fabrics',
    8000000
)

# ini untuk menampilkan ke pelanggan, karena __str__ lebih user-friendly
print(myCouch)

# ini untuk programmer, karena __repr__ lebih detail dan menunjukkan struktur object
print(repr(myCouch))


# FUNGSI DUNDER METHOD:
# 1. __str__ : untuk menampilkan informasi yang user-friendly (untuk di tampilkan PELANGGAN)
# tinggal print(object) saja, 
# maka Python akan otomatis memanggil __str__ method(menampilkan informasi yang user-friendly)


# 2. __repr__ : untuk menampilkan informasi yang lebih detail dan menunjukkan struktur object (untuk di tampilkan PROGRAMMER)
# tinggal print(repr(object)) saja, maka Python akan otomatis memanggil __repr__ method.
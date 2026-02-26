class Phone:
    def __printFullName(self):
        # method dengan double underscore (__) maka Python akan melakukan name mangling
        # nama asli method ini diubah menjadi _Phone__printFullName
        print("Phone: basic model")

class SmartPhone(Phone):
    def __printFullName(self):
        # ini BUKAN override method di class Phone, karena ada double underscore (__),
        # maka Python mengubah namanya menjadi _SmartPhone__printFullName
        print("SmartPhone: flagship model")
        
# membuat object dari class SmartPhone
flagShipPhone1 = SmartPhone()

# memanggil method milik class SmartPhone
# karena sudah di-mangle menjadi _SmartPhone__printFullName
print(flagShipPhone1._SmartPhone__printFullName())

# panggil method milik class Phone | walaupun object-nya SmartPhone,
# method Phone tetap ada dengan nama _Phone__printFullName
print(flagShipPhone1._Phone__printFullName())


# PENJELASAN NAME MANGLING:
# print di class Phone
# __printFullName  →  _Phone__printFullName

# print di class SmartPhone
# __printFullName  →  _SmartPhone__printFullName
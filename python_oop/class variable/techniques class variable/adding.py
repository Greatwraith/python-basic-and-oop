class Wallet:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        

wallet1 = Wallet('Eiger', 550000)
print(f"before adding anything: {wallet1.__dict__}")



print("  ")

# adding a new attributes
# object technique: adding a new attribute ONLY to this object
wallet1.leather = "calf skin"

print(wallet1.__dict__)
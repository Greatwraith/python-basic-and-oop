animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals:
    # untuk setiap animal(satu pe satu) di variabel animals
  chars = chars + len(animal) # menambahkan panjang nama animal ke total chars

print("Total characters: {}, Average length: {}".format(chars, chars/len(animals)))


# 1st LOOP | Lion
# animal = "Lion"
# len("Lion") = 4
# chars = 0 + 4 = 4

# 2nd LOOP | Zebra
# animal = "Zebra"
# len("Zebra") = 5
# chars = 4 + 5 = 9

# 3rd LOOP | Dolphin
# animal = "Dolphin"
# len("Dolphin") = 7
# chars = 9 + 7 = 16

# 4th LOOP | Monkey
# animal = "Monkey"
# len("Monkey") = 6
# chars = 16 + 6 = 22




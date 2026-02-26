pets = "cats and dogs"



indexing = pets.index("d")
indexing2 = pets.index("and")
# we're using the index method to find the index of the first occurrence of "d" and "and"
# in the string "cats and dogs".

is_there_dragon = "dragon" in pets # false. bcuz there's no "dragon" in the string "pets"
is_there_dogs = "dogs" in pets # true. bcuz there's "dogs" in the string "pets"

# we're using the "in" keyword to
# check if the substring "dragon" and "dogs" are exist in the string "pets".



print(indexing)
print(indexing2)
print("Is 'dragon' in pets?", is_there_dragon)
print("Is 'dogs' in pets?", is_there_dogs)




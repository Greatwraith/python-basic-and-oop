string1 = "Greetings, Earthlings"

print(string1[0]) # print index 0


# 2ND EXAMPLE
print(string1[4:8])
# Python slices everything up to, but not including the ending index. 
# Notice in the second example the ending index is 8, but the characters sliced are 4–7.


print (string1[11:]) # print index 0

print(string1[0:5])

# Prints earthlings again
print(string1[-10:])
# If your index is negative, 
# Python counts back from the end of the string instead of the beginning.


# this will print nothing. 
# beyond the end of the strings
# Prints “” 
print(string1[55:])


# Prints “Getns atlns”
print(string1[0::2])

# Prints “sgnilhtraE ,sgniteerG” | PRINT BACKWARD/REVERSE
print(string1[::-1])





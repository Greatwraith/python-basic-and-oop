# Data type mismatch and explicit conversion

# Original code causes a TypeError when combining a string and an integer
# print("5 * 3 = " + (5*3))

# Convert the integer result to a string to fix the error
print("5 * 3 = " + str(5*3))

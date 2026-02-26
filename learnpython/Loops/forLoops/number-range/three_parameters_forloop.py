def to_celsius(x):
  return (x-32)*5/9

for x in range(0, 11, 2):
#   print(x, to_celsius(x))
  print(x,"Fahrenheit","is", to_celsius(x), "Celcius")
  
# x = 10
# (10-32) = -22
# -22 * 5 = -110
# -110 : 9 = 12.22



# range (0, 11, 2)
# if it receives three parameters,
# it will create a sequence starting from the first number and moving towards the second number.
# but this time, the jumps between the numbers will be the size of the third number.
# Again, it will stop before the second number. 

# From
# 0

# 1st
# 0 + 2 = 2

# 2nd
# 2 + 2 = 4

# 3rd
# 4 + 2 = 6  
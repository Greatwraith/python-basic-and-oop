# 1st VERSION:

# set multiples to an empty list
multiples = []

# use for loop to add the first 10 multiples of 2 to the list
for x in range(1, 6): # range(start, stop) 
    multiples.append(x*2) # add the multiples of 2 to the list
    
print(multiples)




# 2nd VERSION: 
# use list comprehension to add the first 10 multiples of 2 to the list 
# list comprehension syntax: [expression for item in iterable if condition]
multiples2 = [x*2 for x in range (1, 6)]
print(multiples2)









# 1st LOOP
# 1st iteration: x = 1, 
# multiples = [2]


# 2nd iteration: x = 2, 
# multiples = [2, 4]


# 3rd iteration: x = 3, 
# multiples = [2, 4, 6]


# 4th iteration: x = 4, 
# multiples = [2, 4, 6, 8]


# 5th iteration: x = 5, 
# multiples = [2, 4, 6, 8, 10]

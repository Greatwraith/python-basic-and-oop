
# the long form version of the code:
print("Long form code result:")
my_list = []
for x in range(1,101):
    if x % 10 == 0:
        my_list.append(x)
print(my_list)

# The list comprehension bellow accomplishes the same result as
print("List comprehension result:")
print([x for x in range(1,101) if x % 10 == 0])


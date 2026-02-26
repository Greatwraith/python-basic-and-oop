def factorial(start, EndBefore):
    product = 1 
    factorial = range(start, EndBefore)
    for n in factorial:
        product = product * n
    return product

result = factorial(1, 5)
print(result)


  # product = 1
# range 1 to 9
# formula 
# productVar = CurrentProduct * EveryRange

# range 1
#  n = 1.
# productVar = 1 * 1 = 1
# currentProduct = 1 

# range 2
# n = 2
# productVar = 1 * 2 = 2
# currentProduct = 2

# range 3
# n = 3 
# productVar = 2 x 3 = 6
# currentProduct = 6

# range 4
# n = 4
# productVar = 6 * 4 = 24
# currentProduct = 24



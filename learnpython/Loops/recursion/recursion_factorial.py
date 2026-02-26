# RECURSIVE FACTORIAL
# - ❌ Does NOT use a loop
# - ✅ Calls itself (factorial(n - 1))
# - ✅ Matches the mathematical definition
# - ❌ Slower in Python
# - ❌ Uses call stack (can hit recursion limit)


def factorial(num):
    if num <= 1:
        return 1
    else:
        return num*factorial(num-1)

printhis = factorial(5)
print(printhis)


# num * fa(num-1)

# n = 5

# 5 * fa(5-1) 
# 5 * 4 * fa(4-1)
# 5 * 4 * 3 * fa(3-1)
# 5 * 4 * 3 * 2 * fa(2-1)
# 5 * 4 * 3 * 2 * 1 

# then print the result of 5 * 4 * 3 * 2 * 1
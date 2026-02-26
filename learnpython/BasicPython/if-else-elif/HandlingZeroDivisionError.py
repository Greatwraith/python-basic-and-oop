# Handling ZeroDivisionError

# Prevent division by zero by ensuring the denominator is not 0
numerator = 7
denominator =0   # example valid denominator

# if the denominator is o/zero, forcebly change it to 1
if denominator == 0:
    denominator = 1  # default value to avoid error


result = numerator / denominator
print(result)

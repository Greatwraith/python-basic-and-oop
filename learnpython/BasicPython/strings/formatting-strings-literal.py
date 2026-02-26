item = "Milk"
amounts = 5
price = amounts * 3.25
tax = price * 0.09
total = price + tax
print(f'item = {item}.  amounts = {amounts}.  price = {price:.2f}.')
print(f'total with tax = {total:.2f}')

# The important difference between f-strings and the format() method is
# that f-strings take the value of the variables from the current context, 
# instead of taking the values from parameters.
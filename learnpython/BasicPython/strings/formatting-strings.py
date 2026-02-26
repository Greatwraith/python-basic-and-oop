# FORMATTING STRING

#  Positional string formatting
name = "Manny"
lucky_number = len(name) * 3
print("Hello {}, your lucky number is {}.".format(name, lucky_number))
# Explanation:
# We have two variables: name and lucky_number.
# The {} symbols are placeholders in the string.
# Python replaces the first {} with name,
# and the second {} with lucky_number.
# The values are filled in order using format().





# Keyword (named) string formatting
name2 = "Ardhan"
print("Hello {name2}, your lucky number is: {my_luckynumber}.".format(name2=name2, my_luckynumber=len(name2)*3))
# Explanation:
# We use names inside the {} brackets.
# Each name matches a value in format().
# Python replaces {name2} with name2,
# and {my_luckynumber} with the lucky number.
# This makes the code easier to read and understand.




# print only with decimal.
price = 7.5
with_tax = price * 1.09
print("Price: {}  With tax: {}".format(price, with_tax))
print("The price : ${:.2f} and with the tax is: ${:.2f}".format(price, with_tax))
# Explanation:
# {:.2f} formats the number to 2 decimal places.
# This is useful for displaying prices or other numbers
# where you want a specific number of decimal places





# fahrenheit to celcius conversion
def to_celcius(fahrenheit):
    celcius = fahrenheit - 32 *5/9
    return celcius

for fahrenheit in range(0, 101, 10):
    print("{:>3} F   |   {:>6.2f} C".format(fahrenheit, to_celcius(fahrenheit)))
# Explanation:
# {:>3} means right-align the number in a field of width 3.
# Examples: "  0", " 10", "100"
#
# {:>6.2f} means right-align the number in a field of width 6,
# display it as a float with 2 digits after the decimal point.
#
# This creates a nicely aligned table of Fahrenheit and Celsius values. formatted table of Fahrenheit and Celsius



firstVar = "Hello"
secondVar = "World"
thirdVar = "Python"

# joining strings using format() and join()
print("{} {} {}".format(firstVar, secondVar, thirdVar)) # Hello World Python

# using join() to concatenate strings with a space in between
joined = " ".join([firstVar, secondVar, thirdVar])
print(joined) # Hello World Python




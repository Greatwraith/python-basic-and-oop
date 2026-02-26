# formating to upper case or lower case
print("formating to upper case or lower case!")

to_lower = "TURN INTO LOWER".lower()
print(to_lower)

mountains_upper = "mountains".upper()  
print(mountains_upper)



print("          ")
print("          ")




# did the user type the correct input, even tho it's in different case?
print("Did the user type the correct input, even tho it's in different case?")

answer = "pyTHON"
if answer.lower() == "python":
    print("user type python")
else:
    print("user did not type python!")




print("          ")
print("          ")



# removing whitespace/stripping spaces
print("removing whitespace/stripping spaces")

whitespaces_on_everycorner = "    whitespace on everycorner   ".strip() 
print(whitespaces_on_everycorner)

whitespaces_on_left = "   whitespaces on left".lstrip()
print(whitespaces_on_left)

whitespaces_on_right = "whitespaces on right    ".strip()
print(whitespaces_on_right)




print("          ")
print("          ")



# counting how many times a substring appears in a string
print("Counting how many times a substring('pizza') appears in a string")

counting = "I like eating pizza because pizza is delicious, my favorites pizza is, italian nyc pizza.".count("pizza")
print(counting)
# pizza appears 4 times in the string.



print("          ")
print("          ")



# whether the string ends with a certain substring
print("Do these strings end with 'land'?")

country1 = "New Zealand".endswith("land")
country2 = "iceland".endswith("land")
country3 = "china".endswith("land")

print(country1) # true
print(country2) # true
print(country3) # false. bcuz "china" does not end with "land".

    

print("          ")
print("          ")

    
    

#  is it numeric or not?
print("Is it numeric or not?")

number1 = "12345".isnumeric()
number2 = "123abc".isnumeric()
print(number1) # true. bcuz "12345" is numeric.
print(number2) # false. bcuz "123abc" is not numeric, it contains letters(abc).




print("          ")
print("          ")





#  if there are only letters in the string
print("Is it numeric or not?")

number1 = "abcde".isalpha()
number2 = "4bcd3".isalpha()
print(number1) # true. bcuz "abcde" is all letters.
print(number2) # false. bcuz "4bcd3" contains numbers (4 and 3).


print("          ")
print("          ")




#  joined strings
print("joined strings!")

joined_string = "_".join(["This", "is", "a", "joined", "string", "with", "underscore"])
print(joined_string) # This_is_a_joined_string






print("          ")
print("          ")






# splitting strings
print("splitting strings!")

string = "This is a splitted string"
split_string = string.split()

second_string = "Another_example_of_splitting_a_string"
split_second_string = second_string.split("_")

print(split_string) # ['This', 'is', 'a', 'splitted', 'string']
print(split_second_string) # ['Another', 'example', 'of', 'splitting', 'a', 'string']
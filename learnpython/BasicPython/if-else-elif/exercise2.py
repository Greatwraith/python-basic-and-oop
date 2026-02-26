number = 12


def number_filled(number):
    if number == 33:
        print("the number is 33")
    elif number <= 6:
        print("the number is less than 6 or 6")
    elif number >= 6 and number <= 32:
        print("the number is less than 6 or six and also greater than 32")
    else:
        print("the number you input is: " + str(number))
        
number_filled(number)
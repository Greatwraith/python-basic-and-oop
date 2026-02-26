# THIS ABOVE IS NOT EFICIENT!!

# name = "Kay"
# number = len(name) * 9
# print("Hello " + name + ". Your lucky number is " + str(number))


# name = "Cameron"
# number = len(name) * 9
# print("Hello " + name + ". Your lucky number is " + str(number))









# THIS IS EFFICIENT
# USE FUNCTION



# 1st VERSION


# def luckynumber(name):
#     number = len(name) * 9
#     print("Hello " + name + " your lucky number is: " + str(number))

# luckynumber("Ardhan")
# luckynumber("ladya")



# 2nd VERSION
# def myluckynumber (name):
#     number = len(name) * 9
#     print("Hello " + name + " your lucky number is: " + str(number))

# firstname = myluckynumber("Ardhan")
# secondname= myluckynumber("Ladya")
# resultOftheProgram = (str(firstname), str(secondname))
# print(resultOftheProgram)
# menghasilkan none,none



# 3rd Version, Everything is organized

greet = "Hello"
luckynum = "your lucky number is: "
good = "enjoy using this program,"


def thirdluckynumber(name):
    number = len(name)*9
    print(greet, name, good, luckynum, str(number))
    
thirdluckynumber("Ardhan")


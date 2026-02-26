# def check_username(username):
#     if len(username) < 8:
#         print("Your usename have to be atleas 8 characters")
#     else:
#         print("your username is VALID")

# check_username("Ardhan_Rahman")



def check_password(password):
    if len(password) < 6 :
        print("your password have to be atleast 6 characters")
    elif len(password) >= 6:
        print("Your password is valid")
    else:
        print("your password is invalid")
        
check_password("")
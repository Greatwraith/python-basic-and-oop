# TUPLES (lists but cannot be changed after they are created)
# Sequences of elements of any type,a and are immutable (cannot be changed after they are created)
# They’re specified using parentheses instead of square brackets.

# Tuples are a special type of data structure in Python that are used when you want to group multiple pieces of information together,
# but you want to ensure that this information remains unchanged. 



fullname = ("Ardhan", "M", "Rahman") # this is a tuple



def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds
result = convert_seconds(5000)

print(result) # (1, 23, 20) 
print(type(result))  # <class 'tuple'> 
# The function returns a tuple containing the hours, minutes, and remaining seconds.


# Each value in the tuple is assigned in order:
# hours → 1, minutes → 23, seconds → 20

    
# Unpacking the tuple into individual variables
# “Save the box first, then open it.”
hours, minutes, seconds = result
print(hours, minutes, seconds)  # 1 23 20


# You can also unpack the returned tuple directly 
# “Open the box immediately and use the contents.”
hours, minutes, seconds = convert_seconds(10000)
# The function runs, returns a tuple, and the values
# are immediately stored in the variables
print(hours, minutes, seconds)  # 2 46 40





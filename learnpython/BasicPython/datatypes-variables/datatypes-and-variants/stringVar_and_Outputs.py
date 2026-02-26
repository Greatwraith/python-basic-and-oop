#String Variables and Output

# 1. Define string variables
# 2.  construct it in order to print it

# Output multiple string variables on a single line to form a sentence 
# Use the plus (+) connector or a comma to connect strings in a print() function 
# Create spaces between variables in  a print() function


salutation = "Sir"
first_name = "M"
middle_name = "Ardhan"
last_name = "Rahman"
suffix = "MSCS"

print(salutation + " " + first_name + ". " + middle_name + " " + last_name + ", " + suffix)
# The comma as a string ", " adds the conventional use of a comma plus a 
# space to separate the last name from the suffix.


# Alternatively, you could use commas in place of the + connector:
print(salutation, first_name, middle_name, last_name,",", suffix)

# However, you will find that this produces a space before a comma within a string.
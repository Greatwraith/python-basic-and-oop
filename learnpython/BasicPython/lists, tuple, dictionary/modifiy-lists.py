number = ["zero", "one", "two", "three", "four", "five"]


# ADDING based on the value
# ADDING A NEW ELEMENT/Elements TO THE END OF THE LIST
number.append("six")
number.append("seven")
print("ADDING A NEW ELEMENT:    " + str(number))


# EDIT
# MODIFYING AN ELEMENT IN THE LIST
drinks = ["water", "juice", "soda", "tea"]
drinks[2] = "coffee" # change the value of the specific index
print("MODIFYING AN ELEMENT:    " + str(drinks))


# INSERTING based on the index number then the value
# INSERTING A NEW ELEMENT TO THE SPECIFIC POSITION IN THE LIST
fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"watermelon") # specific index, new element
fruits.insert(-40, "grape") # negative & out of range, the new element will be added to the beginning of the list
fruits.insert(25, "Peach") # out of range, the new element will be added to the end of the list
print("INSERTING A NEW ELEMENT:    " + str(fruits))


# DELETE
# REMOVING AN ELEMENT FROM THE LIST (based on the Value or the Index)
trash = ["paper", "plastic", "glass", "metal"]
trash.remove("plastic") # remove the specific element
trash.pop(0) # remove the element at the specific index (using index not the value)
print("REMOVING AN ELEMENT:    " + str(trash))




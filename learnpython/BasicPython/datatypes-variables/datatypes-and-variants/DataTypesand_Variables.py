# Data Types and Variables

# Use variables to store values of different data types
# Use basic arithmetic operators with variables to create expressions 
# Use explicit conversion to change a data type from float to string 

hotelRoom = 100 # Cost of the hotel room
tax = hotelRoom * 0.08 # Calculate tax as 8% of the hotel room cost
total = hotelRoom + tax # Total cost including tax
roomGuests = 4 # Number of guests sharing the room

share_per_person = total/roomGuests

# This line outputs the result of the final calculation stored
# in the variable "share_per_person"
print("You have to pay " + str(share_per_person))
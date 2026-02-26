
# definie a function(area_triangle) that takes base and height.
def area_triangle(base, height):
    return base*height/2 # calculate then return base X height / 2 A.K.A the area of a triangle



# defining variables of two area, both area has area_triangles values that are base and height
area_1 = area_triangle(5, 4) #5,4 . base is 5 and height is 4
area_2 = area_triangle(7, 3) #7,3 . base is 7 and height is 3

# defining result/sum variable . inside this variable will be the result of area_1 and area_2 then both of the results will be calculated inside this variable
resultOfboth = area_1 + area_2 # Store the sum of both triangle areas


#printing and calling the function result and convert it to string through str(...)
print("Result: ", str(resultOfboth)) # Print the result (convert to string for concatenation)
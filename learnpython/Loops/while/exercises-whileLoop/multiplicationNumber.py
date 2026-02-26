def multiplication_table(number):
    
    multiplier = 1
    # VarMultiplier = 1
    
    # Run the loop while multiplier is less than or equal to 5
    while multiplier <= 5:
        result = number * multiplier # Calculate the result of number * multiplier
        if result > 25: # Check if the result more than 25
            break# If result > 25, stop the loop immediately
        
        
        # Print the multiplication in the format: number x multiplier = result
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        
        # Increment multiplier 
        multiplier += 1
        # Always VarMultiplier + 1 =.... after every loop.
        # VarMultiplier = VarMultiplier + 1



# multiplication_table(3) 
# AS WE KNOW
# multiplier = 1
# result = number * multiplier

# multiplier = 1
# result = number * multiplier
# result = (number which is 3) 3 X 1 = 3
# then after the result. increment the multiplier.
# so multiplier which is one.    1 + 1 = 2


# then
# RemainMultiplier = 2
# RemainResult = 3
# Result formula
# result = RemainResult * RemainMultiplier

# result = 3 * 2 = 6
# print it
# ReamainMultiplier + 1 
# 2 + 1






# Call the function with 3
multiplication_table(3) 
# Output should be: 
# 3x1=3 
# 3x2=6 
# 3x3=9 
# 3x4=12 
# 3x5=15


# Call the function with 5
multiplication_table(5) 
# Output should be: 
# 5x1=5
# 5x2=10
# 5x3=15
# 5x4=20
# 5x5=25


# Call the function with 8
multiplication_table(8) 
# Output should be:
# 8x1=8
# 8x2=16
# 8x3=24

def is_power_of_two(number):
    # Initial: Var_number = number
    # Var_number will be divided by 2 repeatedly to check if it becomes 1
    
    # Loop while Var_number is not 0 and divisible by 2
    # Var_number != 0 AND Var_number % 2 == 0 → safe check to avoid ZeroDivisionError
    while Var_number != 0 and Var_number % 2 == 0:
        # Var_number = Var_number / 2 → divide by 2 each loop
        Var_number = Var_number / 2
    
    # After loop ends:
    # If Var_number == 1 → original number is a power of 2
    if Var_number == 1:
        return True  # Return True if power of 2
    return False     # Otherwise, return False

# Step-by-step examples

# Example 1: number = 0
# Initial: Var_number = 0
# Check loop: Var_number != 0 AND Var_number % 2 == 0 → 0 != 0 is False → loop skipped
# After loop: Var_number == 1? 0 == 1 → False
# Return False

# Example 2: number = 1
# Initial: Var_number = 1
# Check loop: 1 != 0 AND 1 % 2 == 0 → 1 % 2 = 1 → False → loop skipped
# After loop: Var_number == 1? 1 == 1 → True
# Return True

# Example 3: number = 8
# Initial: Var_number = 8
# Loop 1: Var_number = 8 / 2 = 4
# Loop 2: Var_number = 4 / 2 = 2
# Loop 3: Var_number = 2 / 2 = 1 → loop ends
# After loop: Var_number == 1 → True
# Return True

# Example 4: number = 9
# Initial: Var_number = 9
# Loop check: 9 != 0 AND 9 % 2 == 0 → 9 % 2 = 1 → False → loop skipped
# After loop: Var_number == 1 → 9 == 1 → False
# Return False

# Calls to the function
print(is_power_of_two(0))  # False
print(is_power_of_two(1))  # True
print(is_power_of_two(8))  # True
print(is_power_of_two(9))  # False

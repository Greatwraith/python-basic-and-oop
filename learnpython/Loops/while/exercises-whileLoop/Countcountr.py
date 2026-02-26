def sum_of_integers(n):
    # First, check if n is less than 1
    if n < 1:
        return 0  # If n < 1, there are no positive integers to sum, so return 0

    # Initialize counter variable i and sum accumulator
    i = 1  # Start counting from 1
    sum = 0  # Initialize sum to 0

    # Loop while i is less than or equal to n
    while i <= n:
        sum = sum + i  # Add the current i to the sum. sum = sum + i
        i = i + 1  # Increment i for the next iteration. Var i = i + 1

    # When loop finishes (i > n), return the final sum
    return sum

print(sum_of_integers(3))  # 6
print(sum_of_integers(4))  # 10
print(sum_of_integers(5))  # 15


# Step-by-step example for sum_of_integers(3):
# Initial: Var_i = 1, Var_sum = 0
# Var_i = Var_i + 1 → increment Var_i each loop
# Var_sum = Var_sum + Var_i → accumulate Var_i into Var_sum
# Loop 1: Var_sum = 0 + 1 = 1, Var_i = 1 + 1 = 2
# Loop 2: Var_sum = 1 + 2 = 3, Var_i = 2 + 1 = 3
# Loop 3: Var_sum = 3 + 3 = 6, Var_i = 3 + 1 = 4 → Loop ends because 4 > 3
# Return Var_sum = 6

# Step-by-step example for sum_of_integers(4):
# Initial: Var_i = 1, Var_sum = 0
# Var_i = Var_i + 1 → increment Var_i each loop
# Var_sum = Var_sum + Var_i → accumulate Var_i into Var_sum
# Loop 1: Var_sum = 0 + 1 = 1, Var_i = 1 + 1 = 2
# Loop 2: Var_sum = 1 + 2 = 3, Var_i = 2 + 1 = 3
# Loop 3: Var_sum = 3 + 3 = 6, Var_i = 3 + 1 = 4
# Loop 4: Var_sum = 6 + 4 = 10, Var_i = 4 + 1 = 5 → Loop ends (5 > 4)
# Return Var_sum = 10

# Step-by-step example for sum_of_integers(5):
# Initial: Var_i = 1, Var_sum = 0
# Var_i = Var_i + 1 → increment Var_i each loop
# Var_sum = Var_sum + Var_i → accumulate Var_i into Var_sum
# Loop 1: Var_sum = 0 + 1 = 1, Var_i = 1 + 1 = 2
# Loop 2: Var_sum = 1 + 2 = 3, Var_i = 2 + 1 = 3
# Loop 3: Var_sum = 3 + 3 = 6, Var_i = 3 + 1 = 4
# Loop 4: Var_sum = 6 + 4 = 10, Var_i = 4 + 1 = 5
# Loop 5: Var_sum = 10 + 5 = 15, Var_i = 5 + 1 = 6 → Loop ends (6 > 5)
# Return Var_sum = 15





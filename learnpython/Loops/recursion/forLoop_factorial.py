# ITERATIVE FACTORIAL (Loop-based)
# - ✅ Uses a loop (for)
# - ❌ Does NOT call itself
# - ✅ Faster and safer in Python
# - ✅ Uses constant memory
# - ✅ Commonly used in real programs




def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined by negative numbers")
    
    # You don’t actually need the else after raise. bcuz it'll automatically skip to the next(as long as if is not true)
    else:  ## This block runs ONLY if n is 0 or a positive number
        
        
        result  = 1  # Initialize result to 1. We start from 1 because factorial uses multiplication, (starting from 0 would make everything 0)
        for i in range(1, n +1):  # Loop from 1 up to n (inclusive)
            result = result * i
            # Multiply the current result by i
            # This updates result step by step
            # Example: 1*1 → 1*2 → 2*3 → 6*4 → 24*5 → 120
            
        return result # return the result


bilanganDiisi = factorial(5)
print(bilanganDiisi)



# Loop-based factorial explanation (ITERATIVE)
#
# result starts at 1
# i loops from 1 to n (for n = 5 → 1, 2, 3, 4, 5)
#
# i = 1 → result = 1 * 1 = 1
# i = 2 → result = 1 * 2 = 2
# i = 3 → result = 2 * 3 = 6
# i = 4 → result = 6 * 4 = 24
# i = 5 → result = 24 * 5 = 120
#
# final result returned → 120


def print_range(start, end):
    # Loop through the numbers from start to end
    n = start 
    while n < end:   # ❌ This condition will stop BEFORE reaching 'end', so the last number is missing
        print(n)
        # ❌ Missing n += 1
        # NO INCREMENT!
        # so 'n' never increases → infinite loop if n < end



print_range(1, 5) # should print 1 2 3 4 5
# ❌ This won't print 5 because the loop condition is "n < end", not "n <= end"
# ❌ Without incrementing n, the loop will run forever for n < end


# ❌❌❌DONT RUN THE CODE❌❌❌
# ❌❌❌DONT RUN THE CODE❌❌❌
# ❌❌❌DONT RUN THE CODE❌❌❌
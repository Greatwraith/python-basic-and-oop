# The range() function returns a sequence of numbers, starting from 0 by default, 
# and increments by 1 (by default), 
# STOP ITERATING before it meets a specified number or value.


for iterates_numbers in range(10):
    print(iterates_numbers)
    
# it will iterates numbers
# from 0 and continue before it meets 10.






print(" ")
print(" ")






# 2ND way of writing MY WAY✅

# it will iterate from 1(already input) and continue before it meet 6(already input)
def definedStartandBeforemeet(start, endBeforeMeet):
    
    start_end = range(start, endBeforeMeet)
    
    for counting_process in start_end:
        print(counting_process)
        
definedStartandBeforemeet(1, 6)









print(" ")
print(" ")




# 3RD WAY


given_range = range (5)
# it will iterate from 0 and continue before it meet 5

for iterating in given_range: 
    print(iterating)
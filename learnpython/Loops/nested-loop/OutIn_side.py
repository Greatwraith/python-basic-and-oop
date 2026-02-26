numbers = ['1', '2', '3']
letters = ['a', 'b', 'c']




for letter in letters:           # outer loop
    for number in numbers:   # inner loo      # it'll update the Number, whilst the letter stayed
        print(f"{number}{letter}", end=" ")

# 1a 2a 3a 
# 1b 2b 3b 
# 1c 2c 3c 
# 1d 2d 3d 4d

        
        
# WHATEVER IN THE OUTER LOOP ARE GOING TO STAY
# WHATEVER IN THE INNER ARE GOING TO ITERATE   
        
        
        
        
        

print(" ")
print(" ")


for number in numbers:
    for letter in letters: #It'll update the letter, whilst the number stayed
        print(f"{number}{letter}", end=" ")
print()
# output
# 1a 1b 1c 1d 
# 2a 2b 2c 2d
# 3a 3b 3c 3d 

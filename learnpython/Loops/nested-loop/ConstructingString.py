adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for kata_sifat in adj:
    for buah in fruits:
        print(kata_sifat, buah )
        
        
# We have 2 variables:
# 1. 'kata_sifat' (adjective) such as "red", "big", "tasty"
# 2. 'buah' (fruit) such as "apple", "banana", "cherry"

# we must construct it into a word where all elements in adj must meet all elements in fruits
# Goal: Combine each adjective with all fruits


# formula : # 1st until the last elements in adj + all elements in fruits.
 
# Example: 1ST
# - First adjective: "beautiful"
# - Fruits: "apple", "banana", "cherry"
# Output:
# "beautiful apple", "beautiful banana", "beautiful cherry"

# Example: 2ND
# - Second adjective: "young"
# - Fruits: "apple", "banana", "cherry"
# Output:
# "young apple", "young banana", "young cherry"
def count_letter(text):
    result = {}            # Create an empty dictionary to store letter counts

    for letter in text:    # Loop through each character in the string
        if letter not in result:  
            # If the letter is not yet a key in the dictionary,
            # create it and set its count to 0
            result[letter] = 0

        # Increase the count for this letter by 1
        result[letter] += 1

    # Return the final dictionary
    return result

print(count_letter("aa"))




# inital state
# text = "aa"
# result = {}






# letter = "a"

# "a" not in result  → True
# result["a"] = 0

# result["a"] += 1
# result["a"] = 1
# result is now:
# {"a": 1}




# letter = "a"

# "a" not in result → False (already exists)
# skip creating key ‼️

# result["a"] += 1
# result["a"] = 2

# result is now:
# {"a": 2}



# LAST
# return result
# {"a": 2}
# Dictionary is a collection of key-value pairs. It is unordered, mutable, and indexed.
x = {} # empty dictionary | this is how we create a dictionary
check = type(x)
print(check)  # <class 'dict'>




# CREATING A DICTIONARY | using curly braces {} and key-value pairs separated by a colon :
files_counts = {"python":22, "java": 12, "c++": 15}
print("files_counts:   ", files_counts)  # {'python': 22, 'java': 12, 'c++': 15}



# ACCESSING A VALUE IN THE DICTIONARY | using the key
counting = files_counts["python"]
print("files_counts['python']:   ", counting) # 22



# CHECKING IF A KEY EXISTS IN THE DICTIONARY | using the 'in' keyword
istherepython = "python" in files_counts # True
istherehtml = "html" in files_counts # False
print("Is 'python' in files_counts? :   ", istherepython) # True
print("Is 'html' in files_counts? :   ", istherehtml) # False




# ADDING | MODIFYING | DELETING KEY-VALUE PAIRS IN THE DICTIONARY

# ADDING A NEW KEY-VALUE PAIR TO THE DICTIONARY | using the assignment operator =
files_counts["ruby"] = 5 # adding a new key-value pair to the dictionary
print("After adding 'ruby':   ", files_counts) # {'python': 22, 'java': 12, 'c++': 15, 'ruby': 5}



# MODIFYING THE VALUE OF AN EXISTING KEY IN THE DICTIONARY | using the assignment operator =
files_counts["python"] = 30 # modifying the value of an existing key
print("After modifying 'python':   ", files_counts) # {'python': 30, 'java': 12, 'c++': 15, 'ruby': 5}



# DELETING A KEY-VALUE PAIR FROM THE DICTIONARY | using the 'del' keyword
del files_counts["java"] # deleting a key-value pair from the dictionary using the 'del' keyword
print("After deleting 'java':   ", files_counts) # {'python': 30, 'c++': 15, 'ruby': 5}




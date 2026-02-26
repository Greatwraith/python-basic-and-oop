# if a for loop can fit in a single line,
# then you can use a list comprehension to create a new list based on the original list.


languages = ["Python", "Java", "C++", "Dart"]


lengths = [len(language) for language in languages]

print(lengths)


# 1st iteration: language = "Python", lengths = [6]
# 2nd iteration: language = "Java", lengths = [6, 4]
# 3rd iteration: language = "C++", lengths = [6, 4, 3]
# 4th iteration: language = "Dart", lengths = [6, 4, 3, 4]

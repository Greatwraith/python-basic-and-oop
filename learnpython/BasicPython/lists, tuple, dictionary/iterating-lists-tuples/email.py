
def full_emails(people):
    result = []
    for fullName, email in people:
        result.append("{} <{}>".format(fullName, email))
    return result

printThis = full_emails([("ardhan@example.com", "Ardhan M Rahman"), ("john@example.com", "John Doe")])
print(printThis)





def full_emails(people):
    result = []

    # Loop through each item in the 'people' list
    # Each item is a tuple that contains two values: f(fullName, email)
    for fullName, email in people:
        # Unpack the tuple:
        # fullName gets the first value
        # email gets the second value

        # Create a formatted string in the form:
        # "Full Name <email@example.com>"
        formatted_email = "{} <{}>".format(fullName, email)

        # Add the formatted string to the result list
        result.append(formatted_email)

    # After the loop finishes, return the list of formatted email strings
    return result


# Call the function with a list of tuples
# Each tuple represents one person and contains:
# (email address, full name)
printThis = full_emails([
    ("ardhan@example.com", "Ardhan M Rahman"),
    ("john@example.com", "John Doe")
])

# Print the returned list
print(printThis)

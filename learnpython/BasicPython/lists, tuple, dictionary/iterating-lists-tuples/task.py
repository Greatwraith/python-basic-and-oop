def skip_elements(elements):
    # Create an empty list to store the elements we want to keep
    result = []

    # Loop through the list using enumerate()
    # enumerate() gives us: index (position) and element (value)
    for index, element in enumerate(elements):
        
        # Check if the index is even
        # Even positions: 0, 2, 4, 6, ...
        if index % 2 == 0:
            # If the index is even, add the element to the result list
            result.append(element)

    # After the loop finishes, return the result list
    return result


print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))
# ['a', 'c', 'e', 'g']

print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))
# ['Orange', 'Strawberry', 'Peach']

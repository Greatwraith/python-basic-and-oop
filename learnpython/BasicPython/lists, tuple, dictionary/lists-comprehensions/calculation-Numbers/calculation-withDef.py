def odd_numbers(n):
	return [x for x in range(1, n + 1) if x % 2 != 0]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []


# 1st iteration: x = 5, odd_numbers = [1, 3, 5]
# 2nd iteration: x = 10, odd_numbers = [1, 3, 5, 7, 9]
# 3rd iteration: x = 11, odd_numbers = [1, 3, 5, 7, 9, 11]
# 4th iteration: x = 1, odd_numbers = [1]
# 5th iteration: x = -1, odd_numbers = [] (karena tidak ada angka ganjil yang kurang dari atau sama dengan -1)
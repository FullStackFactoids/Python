numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]
print(squares)  # Output: [1, 4, 9, 16, 25]

#Fun Facts
numbers = [1, 2, 3, 4, 5]
even_squares = [n**2 for n in numbers if n % 2 == 0]
print(even_squares)  # Output: [4, 16]
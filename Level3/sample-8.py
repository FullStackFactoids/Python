def square(n):
    return n**2

numbers = [1, 2, 3, 4, 5]
squares = map(square, numbers)
print(list(squares))

#FUN FACTS
def add(a, b):
    return a + b

numbers1 = [1, 2, 3, 4, 5]
numbers2 = [6, 7, 8, 9, 10]
result = map(add, numbers1, numbers2)
print(list(result))  # Output: [7, 9, 11, 13, 15]

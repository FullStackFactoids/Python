square = lambda x: x**2
print(square(5)) # Output: 25

#Fun Facts
def apply_func(x, func):
    return func(x)

result = apply_func(5, lambda x: x**2)
print(result)  # Output: 25
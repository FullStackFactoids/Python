def my_function(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key} = {value}")

my_function("Hello", "World", name="John", age=36)
# Output:
# Hello
# World
# name = John
# age = 36

# FUN FACTS
def my_function(*args):
    for arg in args:
        print(arg)

my_function("Hello", "World", "I", "am", "John")
# Output:
# Hello
# World
# I
# am
# John
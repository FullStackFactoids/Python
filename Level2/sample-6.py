class MyClass:
    def __init__(self, name):
        self.name = name

my_instance = MyClass("John") # Create an instance of MyClass

#Fun Facts
class MyClass:
    def __init__(self, x):
        self.x = x

a = MyClass(1)
b = MyClass(2)
a.x = 3  # This doesn't affect b.x
print(a.x, b.x)  # Output: 3 2
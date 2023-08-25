class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
print(p1.name) # Output: John
print(p1.age) # Output: 36

#FUN FACTS

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

p1 = Person("John", 36)
p1.greet() # Output: Hello, my name is John and I am 36 years old.

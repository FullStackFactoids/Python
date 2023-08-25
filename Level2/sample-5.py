class MyClass:
    def __init__(self, name):
        self.name = name

#Fun Facts
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

my_dog = Dog()
print(my_dog.speak())  # Output: "Woof!"
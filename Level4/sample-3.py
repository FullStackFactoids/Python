class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'

obj = MyClass()
print(obj.method())
print(obj.classmethod())
print(obj.staticmethod())
# Output:
# ('instance method called', <__main__.MyClass object at 0x10a6897f0>)
# ('class method called', <class '__main__.MyClass'>)
# static method called

# FUN FACTS
class MyClass:
    @staticmethod
    def greet(name):
        print(f"Hello, {name}!")

MyClass.greet("Alice")
# Output:
# Hello, Alice
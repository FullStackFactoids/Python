class MyClass:
    __slots__ = ['name', 'age']

obj = MyClass()
obj.name = "Alice"
obj.age = 30
# obj.address = "Unknown"  # This will raise an AttributeError
print(obj.name, obj.age)  # Output: Alice 30

# Fun Facts
class MyClassWithoutSlots:
    pass

obj = MyClassWithoutSlots()
obj.name = "Bob"
obj.address = "Unknown"  # This works fine
print(obj.name, obj.address)  # Output: Bob Unknown
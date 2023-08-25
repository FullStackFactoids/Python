a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)  # True
print(a is b)  # True

print(a == c)  # True
print(a is c)  # False

#FUN FACTS

a = None
print(a is None)  # True
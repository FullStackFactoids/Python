class Product:
    def __init__(self):
        self.x = 10

    def __call__(self, y):
        return self.x * y

p = Product()
print(p(5))  # Output: 50

#FUN FACTS
class Adder:
    def __call__(self, x, y):
        return x + y

add = Adder()
print(add(5, 3))  # Output: 8
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        self._name = value

    @name.deleter
    def name(self):
        del self._name

p = Person("John")
print(p.name)  # Output: John
p.name = "Alice"
print(p.name)  # Output: Alice
del p.name

# FUN FACTS

class Celsius:
    def __init__(self, temperature = 0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    # new update
    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value

c = Celsius(25)  # This will work fine
# But this will raise a ValueError:
c = Celsius(-300)  # "Temperature below -273.15 is not possible"
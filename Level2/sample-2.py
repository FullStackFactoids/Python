try:
    x = 1 / 0
except ZeroDivisionError:
    x = 0

#Fun Facts
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Can't divide by zero!") # Output: Can't divide by zero!
except TypeError:
    print("x and y must be numbers!")  # This won't be executed
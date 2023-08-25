try:
    x = 1 / 0
except ZeroDivisionError as e:
    print("Caught an exception: ", e)
# Output: Caught an exception:  division by zero

# FUN FACTS

try:
    x = 1 / 0
except (ZeroDivisionError, TypeError) as e:
    print("Caught an exception: ", e)
# Output: Caught an exception:  division by zero
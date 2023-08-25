try:
    x = 1 / 0
except ZeroDivisionError:
    print("You can't divide by zero!") # Output: You can't divide by zero!

#FUN FACTS
try:
    x = 1 / 0
except (ZeroDivisionError, TypeError):
    print("An error occurred!") # Output: An error occurred!"

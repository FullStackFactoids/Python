def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

#FUN FACTS
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_goodbye():
    print("Goodbye!")

say_goodbye = my_decorator(say_goodbye)

say_goodbye()
# Output:
# Something is happening before the function is called.
# Goodbye!
#Something is happening after the function is called.
def my_decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before the function call
# Hello!
# After the function call

# FUN FACTS

def timing_decorator(func):
    import time
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Time taken: ", end - start)
    return wrapper

@timing_decorator
def my_function():
    num_list = [x for x in range(1000000)]
    print("Sum of all the numbers: ", sum(num_list))

my_function()
# Output:
# Sum of all the numbers:  499999500000
# Time taken:  0.1019291877746582

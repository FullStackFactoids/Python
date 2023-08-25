def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for number in count_up_to(5):
    print(number) # Output: 1 2 3 4 5

#FUN FACTS
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

f = fibonacci()

for i in range(10):
    print(next(f))  # Output: 0 1 1 2 3 5 8 13 21 34
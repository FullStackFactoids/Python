def my_generator():
    for i in range(3):
        yield i

for item in my_generator():
    print(item)
# Output:
# 0
# 1
# 2

# FUN FACTS

def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1

for num in countdown(10):
    print(num)
# Output:
# Starting
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
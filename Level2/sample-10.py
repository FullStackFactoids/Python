def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("radar"))  # True

#Fun Facts

my_list = [1, 2, 3, 4, 5]
reversed_list = my_list[::-1]
print(reversed_list)  # Output: [5, 4, 3, 2, 1]

my_string = "Python"
reversed_string = my_string[::-1]
print(reversed_string)  # Output: "nohtyP"

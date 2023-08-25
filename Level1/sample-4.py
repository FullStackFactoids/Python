result = 3 + 4

#Fun Facts
import sys

sys.set_int_max_str_digits(1000000)  # Increase the limit to 1,000,000 digits
result = 2**1000000
print(len(str(result)))  # prints the number of digits in the result"
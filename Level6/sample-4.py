# Assuming a C shared library 'libexample.so' with a function 'add' defined as:
# int add(int a, int b) { return a + b; }
import ctypes

lib = ctypes.CDLL('./libexample.so')
result = lib.add(2, 3)
print(result)  # Output: 5

# Fun Facts
import ctypes

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]

point = POINT(10, 20)
print(point.x, point.y)  # Output: 10 20
import unittest

def fun(x):
    return x + 1

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)

if __name__ == '__main__':
    unittest.main()
# This will run the test case and output the results

#Fun Facts

import unittest

def fun(x):
    return x + 1

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 5)

if __name__ == '__main__':
    unittest.main()
# This will run the test case and output the results. The test will fail because fun(3) is not equal to 5.
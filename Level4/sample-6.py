class MyDict:
    def __init__(self):
        self._dict = {}

    def __getitem__(self, key):
        return self._dict[key]

    def __setitem__(self, key, value):
        self._dict[key] = value

d = MyDict()
d["a"] = 1
print(d["a"])  # Output: 1

# FUN FACTS

class MyList:
    def __init__(self):
        self._list = []

    def __getitem__(self, index):
        return self._list[index]

    def __setitem__(self, index, value):
        self._list[index] = value

l = MyList()
l[0] = 1
print(l[0])  # This will raise an IndexError
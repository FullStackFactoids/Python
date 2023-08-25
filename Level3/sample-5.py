import copy

original = [[1], [2], [3]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

original.append([4])
original[0].append(2)

print("Original:", original)  # [[1, 2], [2], [3], [4]]
print("Shallow:", shallow) # [[1, 2], [2], [3]]
print("Deep:", deep)    # [[1], [2], [3]]

#FUN FACTS
import copy

original = [[1], [2], [3]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

print("Shallow:", shallow)
print("Deep:", deep)
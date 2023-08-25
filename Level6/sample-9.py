import gc

# Force a garbage collection cycle
gc.collect()
print(gc.get_stats())  # Output: [{'collections': xx, 'collected': xx, 'uncollectable': xx}, ...]

# Fun Facts

import gc

class CircularReference:
    def __init__(self):
        self.circular_ref = self

obj = CircularReference()
del obj

print(gc.collect())  # Output: 1 (or more, indicating the number of objects collected)
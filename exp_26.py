import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Slicing
print("Slice:", arr[1:4])

# Integer indexing
print("Integer indexing:", arr[[0, 2, 4]])

# Boolean indexing
print("Boolean indexing:", arr[arr > 25])


# Slice: [20 30 40]
# Integer indexing: [10 30 50]
# Boolean indexing: [30 40 50]

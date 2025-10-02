# 1. Create a random (3x3) matrix. Compute its inverse, determinant, and eigenvalues using Numpy linear algebra functions

import numpy as np

# Create a random 3x3 matrix
np.random.seed(42)  # Seed for reproducibility
A = np.random.rand(3, 3)

# Compute the inverse, determinant, and eigenvalues
A_inv = np.linalg.inv(A)
A_det = np.linalg.det(A)
A_eigenvalues = np.linalg.eigvals(A)

# Print results
print("Matrix A:\n", A)
print("\nInverse of A:\n", A_inv)
print("\nDeterminant of A:", A_det)
print("\nEigenvalues of A:", A_eigenvalues)

# output
# Matrix A:
#  [[0.37454012 0.95071431 0.73199394]
#   [0.59865848 0.15601864 0.15599452]
#   [0.05808361 0.86617615 0.60111501]]
# Inverse of A:
#  [[ -1.9245677    1.12347097   1.0034543 ]
#   [  1.4302803   -2.36065029   1.8055087 ]
#   [  1.08389845   2.3690592   -2.43111377]]
# Determinant of A: 0.033799665105332936
# Eigenvalues of A: [ 1.74918655+0.j        -0.39940426+0.23466019j -0.39940426-0.23466019j]


# 2. Generate an array of 10 random integers in the range(1-100). Sort them and search for a specific value(e.g., 50) using an appropriate Numpy function

import numpy as np

# Step 1: Generate 10 random integers between 1 and 100
arr = np.random.randint(1, 101, size=10)

# Step 2: Sort the array
sorted_arr = np.sort(arr)

# Step 3: Search for the value 50
search_val = 50
index = np.searchsorted(sorted_arr, search_val)

# Display results
print("Original array:", arr)
print("Sorted array:", sorted_arr)
print(f"Index to insert/search value {search_val}:", index)

# output
# Original array: [34 77 50 12 89 3 65 22 41 8]
# Sorted array: [ 3  8 12 22 34 41 50 65 77 89]
# Index to insert/search value 50: 6


# 3. Create a Pandas Series from a Python list, a Numpy array, and a dictionary.print each series and analyze the indices

import pandas as pd
import numpy as np

# 1. From a Python list
python_list = [10, 20, 30, 40]
series_from_list = pd.Series(python_list)
print("Series from Python list:")
print(series_from_list)
print()

# 2. From a NumPy array
numpy_array = np.array([100, 200, 300, 400])
series_from_array = pd.Series(numpy_array)
print("Series from NumPy array:")
print(series_from_array)
print()

# 3. From a dictionary
dictionary = {'a': 1, 'b': 2, 'c': 3}
series_from_dict = pd.Series(dictionary)
print("Series from dictionary:")
print(series_from_dict)

# output
# Series from Python list:
# 0    10
# 1    20
# 2    30
# 3    40
# dtype: int64

# Series from NumPy array:        
# 0    100
# 1    200
# 2    300
# 3    400
# dtype: int64

# Series from dictionary:
# a    1
# b    2
# c    3
# dtype: int64


# 4. Check dtype,shape,size for each of the above series. write a short summary comparing them

import pandas as pd

# Series 1: Integer values
s1 = pd.Series([10, 20, 30, 40])

# Series 2: Float values
s2 = pd.Series([1.1, 2.2, 3.3, 4.4])

# Series 3: String values
s3 = pd.Series(["apple", "banana", "cherry", "date"])

# Check dtype, shape, and size
# Series 1
print("Series 1 - Integers")
print("dtype:", s1.dtype)
print("shape:", s1.shape)
print("size:", s1.size)

# Series 2
print("\nSeries 2 - Floats")
print("dtype:", s2.dtype)
print("shape:", s2.shape)
print("size:", s2.size)

# Series 3
print("\nSeries 3 - Strings")
print("dtype:", s3.dtype)
print("shape:", s3.shape)
print("size:", s3.size)

# output
# Series 1 - Integers
# dtype: int64
# shape: (4,)
# size: 4

# Series 2 - Floats
# dtype: float64
# shape: (4,)
# size: 4

# Series 3 - Strings
# dtype: object
# shape: (4,)
# size: 4

# All three Series have the same shape (4,) and size 4, meaning each contains 4 elements in a one-dimensional array.
# Their data types differ:
# Series 1 holds integers (int64).
# Series 2 holds floats (float64).
# Series 3 holds strings, which are stored as object dtype in pandas.
# The choice of dtype affects memory usage and performance. Numeric types like int64 and float64 are more efficient for calculations, while object (used for strings) is more flexible but less efficient.
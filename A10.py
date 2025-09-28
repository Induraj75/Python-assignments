# 1. Create arrays using empty,zeros, ones, print their values,shapes,and default datatypes.
import numpy as np
# Create an empty array of shape (3, 3)
empty_array = np.empty((3, 3))
print("Empty Array:")
print(empty_array)
print("Shape:", empty_array.shape)
print("Data type:", empty_array.dtype)
print()

# Create a zeros array of shape (3, 3)
zeros_array = np.zeros((3, 3))
print("Zeros Array:")
print(zeros_array)
print("Shape:", zeros_array.shape)
print("Data type:", zeros_array.dtype)
print()

# Create a ones array of shape (3, 3)
ones_array = np.ones((3, 3))
print("Ones Array:")
print(ones_array)
print("Shape:", ones_array.shape)
print("Data type:", ones_array.dtype)

# output
# Empty Array:
# [[6.95239144e-310 6.95240971e-310 6.95240971e-310]
#  [6.95240970e-310 6.95240971e-310 6.95240970e-310]
#  [6.95240969e-310 6.95240969e-310 6.95240971e-310]]
# Shape: (3, 3)
# Data type: float64

# Zeros Array:
#  [0. 0. 0.]
#  [0. 0. 0.]]
# Shape: (3, 3)
# Data type: float64

# Ones Array:
# [[1. 1. 1.]
#  [1. 1. 1.]
#  [1. 1. 1.]]
# Shape: (3, 3)
# Data type: float64

# note
# empty() creates an array without initializing entries (values can be random/garbage).
# zeros() creates an array filled with 0.
# ones() creates an array filled with 1.
# The default data type is usually float64.


# 2. create a structured array with fields for name(string) and age(int). Insert a few records and then display them. 

import numpy as np

# Define the data type for the structured array
dtype = [('name', 'U10'), ('age', 'i4')]

# Create an empty structured array with 3 records
people = np.array([('Alice', 25), ('Bob', 30), ('Charlie', 35)], dtype=dtype)

# Display the structured array
print(people)

# output
# [('Alice', 25) ('Bob', 30) ('Charlie', 35)]

# how to handle heterogeneous data with numpy

import numpy as np

# Define the data type with field names and their types
dtype = [
    ('name', 'U10'),   # Unicode string up to length 10
    ('age', 'i4'),     # 4-byte integer
    ('height', 'f4'),  # 4-byte float
    ('is_student', '?') # Boolean
]

# Create the structured array with some records
data = np.array([
    ('Alice', 25, 5.5, True),
    ('Bob', 30, 6.1, False),
    ('Charlie', 35, 5.9, True)
], dtype=dtype)

# Display the entire array
print("Complete structured array:")
print(data)

# Access a field (e.g. all names)
print("\nNames:", data['name'])

# Access a specific record
print("\nRecord of second person:", data[1])

# Access a specific field of a record
print("\nAge of first person:", data[0]['age'])

# output
# Complete structured array:
# [('Alice', 25, 5.5,  True) ('Bob', 30, 6.1, False)
#  ('Charlie', 35, 5.9,  True)]
# Names: ['Alice' 'Bob' 'Charlie']
# Record of second person: ('Bob', 30, 6.1, False)
# Age of first person: 25


# 3. create arrays using arrange,linspace, and logspace to illustrate each function. plot these arrays(optional) to visualize differences in spacing

import numpy as np
import matplotlib.pyplot as plt

# Using arange: generates values from start to stop with a fixed step size
arr_arange = np.arange(1, 10, 1)  # from 1 to 9 with step 1

# Using linspace: generates a specified number of evenly spaced points between start and stop
arr_linspace = np.linspace(1, 10, 10)  # 10 points from 1 to 10, inclusive

# Using logspace: generates numbers spaced evenly on a log scale
arr_logspace = np.logspace(0, 1, 10)  # 10 points from 10^0=1 to 10^1=10

# Plotting to visualize
plt.figure(figsize=(10, 6))
plt.plot(arr_arange, np.zeros_like(arr_arange), 'o', label='arange (step=1)')
plt.plot(arr_linspace, np.ones_like(arr_linspace)*1, 's', label='linspace (10 points)')
plt.plot(arr_logspace, np.ones_like(arr_logspace)*2, 'd', label='logspace (10 points)')

plt.yticks([0, 1, 2], ['arange', 'linspace', 'logspace'])
plt.xlabel('Value')
plt.title('Differences in Spacing: arange, linspace, logspace')
plt.legend()
plt.grid(True)
plt.show()

# output
# The arange points (circles) are evenly spaced with a fixed step size of 1, from 1 up to 9.
# The linspace points (squares) are exactly 10 points evenly spaced between 1 and 10, inclusive.
# The logspace points (diamonds) are spaced exponentially, clustering more near 1 and spreading out towards 10.

# Visual Description:
# Y-axis labels:  
# 0 — arange (step=1)  
# 1 — linspace (10 points)  
# 2 — logspace (10 points)  

# On the x-axis, points appear as:  
# - arange: 1, 2, 3, ..., 9 (equally spaced)  
# - linspace: 1, 2, 3, ..., 10 (equally spaced including 10)  
# - logspace: 1, ~1.3, ~1.7, ..., 10 (values increase exponentially)

# 4. Create a 2D array of shape(3x1) and a 1D array of shape(3,). show how addition or multiplication automatically broadcasts. 

import numpy as np
# 2D array of shape (3, 1)
arr_2d = np.array([[1],
                   [2],
                   [3]])

# 1D array of shape (3,)
arr_1d = np.array([10, 20, 30])

# Addition
result_add = arr_2d + arr_1d

# Multiplication
result_mul = arr_2d * arr_1d

print("2D array (3x1):\n", arr_2d)
print("1D array (3,):\n", arr_1d)

print("\nAddition result:\n", result_add)
print("\nMultiplication result:\n", result_mul)

# output
# 2D array (3x1):
#  [[1]
#   [2]
#   [3]]
# 1D array (3,):
#  [10 20 30]

# Addition result:
#  [[11 21 31]
#   [12 22 32]
#   [13 23 33]]

# Multiplication result:
#  [[10 20 30]
#   [20 40 60]
#   [30 60 90]]
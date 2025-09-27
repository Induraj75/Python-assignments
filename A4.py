# 1. Take inputs of various types (string,float,etc.). convert them into at least three different types (eg., float -> int -> str) print them out to verify

# Take various inputs
string_input = input("Enter a string: ")
float_input = float(input("Enter a float number: "))
int_input = int(input("Enter an integer: "))

# Convert string input into different types
try:
    str_to_int = int(string_input)
except ValueError:
    str_to_int = "Conversion to int failed"
try:
    str_to_float = float(string_input)
except ValueError:
    str_to_float = "Conversion to float failed"
str_to_list = list(string_input)

# Convert float input into different types
float_to_int = int(float_input)
float_to_str = str(float_input)
float_to_bool = bool(float_input)

# Convert int input into different types
int_to_float = float(int_input)
int_to_str = str(int_input)
int_to_bool = bool(int_input)

# Print the conversions
print("\nConversions from string input:")
print(f"Original string: {string_input}")
print(f"To int: {str_to_int}")
print(f"To float: {str_to_float}")
print(f"To list: {str_to_list}")

print("\nConversions from float input:")
print(f"Original float: {float_input}")
print(f"To int: {float_to_int}")
print(f"To str: {float_to_str}")
print(f"To bool: {float_to_bool}")

print("\nConversions from int input:")
print(f"Original int: {int_input}")
print(f"To float: {int_to_float}")
print(f"To str: {int_to_str}")
print(f"To bool: {int_to_bool}")


# output
# Enter a string: 123.45
# Enter a float number: 56.78
# Enter an integer: 42

# Conversions from string input:
# Original string: 123.45
# To int: Conversion to int failed
# To float: 123.45
# To list: ['1', '2', '3', '.', '4', '5']

# Conversions from float input:
# Original float: 56.78
# To int: 56
# To str: 56.78
# To bool: True

# Conversions from int input:
# Original int: 42
# To float: 42.0
# To str: 42
# To bool: True


# 2. create a small table or list demonstrating how python evaluates expressions of mixed  data types (e.g., int + float, float + complex, etc.). Summarize any interesting findings.

# | Expression     | Result Value | Result Type | Explanation                                        |
# | -------------- | ------------ | ----------- | -------------------------------------------------- |
# | `3 + 4`        | `7`          | `int`       | Both operands are `int`, result is `int`.          |
# | `3 + 4.5`      | `7.5`        | `float`     | `int` is promoted to `float`, result is `float`.   |
# | `4.5 + 2.5`    | `7.0`        | `float`     | Both operands are `float`, result is `float`.      |
# | `3 + 2 + 4.5`  | `9.5`        | `float`     | `int`s combined first, then promoted to `float`.   |
# | `3 + 4j`       | `(3+4j)`     | `complex`   | `int` promoted to `complex`, result is complex.    |
# | `4.5 + 2j`     | `(4.5+2j)`   | `complex`   | `float` promoted to `complex`, result complex.     |
# | `3 + 4.5 + 2j` | `(7.5+2j)`   | `complex`   | Mixed `int`, `float`, and `complex` -> `complex`.  |
# | `3 + True`     | `4`          | `int`       | `True` is `1` (int), so addition behaves like int. |

# Interesting Findings:

# Python automatically promotes types in mixed expressions in the order: int → float → complex.
# Boolean values are treated as integers (True = 1, False = 0).
# Once a complex number is involved, the entire expression's result is complex.
# Chaining operations respects this hierarchy, promoting types as needed.


# 3. Write a Python script demonstrating each category of operator with examples. print out the results and comment on each line to explain.

# Arithmetic Operators
a = 10
b = 3

print("Arithmetic Operators:")
print(f"a + b = {a + b}  # Addition: 10 + 3 = 13")
print(f"a - b = {a - b}  # Subtraction: 10 - 3 = 7")
print(f"a * b = {a * b}  # Multiplication: 10 * 3 = 30")
print(f"a / b = {a / b}  # Division (float): 10 / 3 = {a / b}")
print(f"a // b = {a // b}  # Floor Division (integer division): 10 // 3 = 3")
print(f"a % b = {a % b}  # Modulus (remainder): 10 % 3 = 1")
print(f"a ** b = {a ** b}  # Exponentiation: 10 ** 3 = 1000\n")

# Comparison Operators
print("Comparison Operators:")
print(f"a == b: {a == b}  # Equal to: 10 == 3 is False")
print(f"a != b: {a != b}  # Not equal to: 10 != 3 is True")
print(f"a > b: {a > b}    # Greater than: 10 > 3 is True")
print(f"a < b: {a < b}    # Less than: 10 < 3 is False")
print(f"a >= b: {a >= b}  # Greater than or equal to: 10 >= 3 is True")
print(f"a <= b: {a <= b}  # Less than or equal to: 10 <= 3 is False\n")

# Logical Operators
x = True
y = False

print("Logical Operators:")
print(f"x and y: {x and y}  # Logical AND: True and False is False")
print(f"x or y: {x or y}    # Logical OR: True or False is True")
print(f"not x: {not x}      # Logical NOT: not True is False\n")

# Bitwise Operators
print("Bitwise Operators:")
a = 5  # binary: 0101
b = 3  # binary: 0011

print(f"a & b = {a & b}  # Bitwise AND: 0101 & 0011 = 0001 (1)")
print(f"a | b = {a | b}  # Bitwise OR: 0101 | 0011 = 0111 (7)")
print(f"a ^ b = {a ^ b}  # Bitwise XOR: 0101 ^ 0011 = 0110 (6)")
print(f"~a = {~a}          # Bitwise NOT: ~0101 = 1010 (-6 in two's complement)")
print(f"a << 1 = {a << 1}  # Left shift: 0101 << 1 = 1010 (10)")
print(f"a >> 1 = {a >> 1}  # Right shift: 0101 >> 1 = 0010 (2)\n")

# Assignment Operators
print("Assignment Operators:")
c = 10
print(f"c = {c}  # Simple assignment")

c += 5
print(f"c += 5: {c}  # Equivalent to c = c + 5")

c -= 3
print(f"c -= 3: {c}  # Equivalent to c = c - 3")

c *= 2
print(f"c *= 2: {c}  # Equivalent to c = c * 2")

c /= 4
print(f"c /= 4: {c}  # Equivalent to c = c / 4")

c %= 3
print(f"c %= 3: {c}  # Equivalent to c = c % 3")

c **= 2
print(f"c **= 2: {c}  # Equivalent to c = c ** 2")

c //= 2
print(f"c //= 2: {c}  # Equivalent to c = c // 2\n")

# Identity Operators
print("Identity Operators:")
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(f"x is y: {x is y}  # True because y references the same object as x")
print(f"x is z: {x is z}  # False because z is a different object")
print(f"x is not z: {x is not z}  # True because they are different objects\n")

# Membership Operators
print("Membership Operators:")
lst = [1, 2, 3, 4, 5]

print(f"3 in lst: {3 in lst}  # True because 3 is in the list")
print(f"6 not in lst: {6 not in lst}  # True because 6 is not in the list")

#  output
# Arithmetic Operators:
# a + b = 13  # Addition: 10 + 3 = 13
# a - b = 7  # Subtraction: 10 - 3 = 7
# a * b = 30  # Multiplication: 10 * 3 = 30
# a / b = 3.3333333333333335  # Division (float): 10 / 3 = 3.3333333333333335
# a // b = 3  # Floor Division (integer division): 10 // 3 = 3
# a % b = 1  # Modulus (remainder): 10 % 3 = 1
# a ** b = 1000  # Exponentiation: 10 ** 3 = 1000

# Comparison Operators:
# a == b: False  # Equal to: 10 == 3 is False
# a != b: True  # Not equal to: 10 != 3 is True
# a > b: True    # Greater than: 10 > 3 is True
# a < b: False    # Less than: 10 < 3 is False
# a >= b: True  # Greater than or equal to: 10 >= 3 is True
# a <= b: False  # Less than or equal to: 10 <= 3 is False

# Logical Operators:
# x and y: False  # Logical AND: True and False is False
# x or y: True    # Logical OR: True or False is True
# not x: False      # Logical NOT: not True is False

# Bitwise Operators:
# a & b = 1  # Bitwise AND: 0101 & 0011 = 0001 (1)
# a | b = 7  # Bitwise OR: 0101 | 0011 = 0111 (7)
# a ^ b = 6  # Bitwise XOR: 0101 ^ 0011 = 0110 (6)
# ~a = -6          # Bitwise NOT: ~0101 = 1010 (-6 in two's complement)
# a << 1 = 10  # Left shift: 0101 << 1 = 1010 (10)
# a >> 1 = 2  # Right shift: 0101 >> 1 = 0010 (2)

# Assignment Operators:
# c = 10  # Simple assignment
# c += 5: 15  # Equivalent to c = c + 5
# c -= 3: 12  # Equivalent to c = c - 3
# c *= 2: 24  # Equivalent to c = c * 2
# c /= 4: 6.0  # Equivalent to c = c / 4
# c %= 3: 0.0  # Equivalent to c = c % 3
# c **= 2: 0.0  # Equivalent to c = c ** 2
# c //= 2: 0.0  # Equivalent to c = c // 2

# Identity Operators:
# x is y: True  # True because y references the same object as x
# x is z: False  # False because z is a different object
# x is not z: True  # True because they are different objects

# Membership Operators:
# 3 in lst: True  # True because 3 is in the list
# 6 not in lst: True  # True because 6 is not in the list


# 4.  Take any sample string and a sample list of numbers. Demonstrate forward slicing, backward slicing, skipping elements,etc.  

sample_string = "Hello, World!"
sample_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# 1. Forward slicing
# Extract from index 2 to 6 (not including 6)
print(sample_string[2:6])  # 'llo,'
print(sample_list[2:6])    # [30, 40, 50, 60]

# 2. Backward slicing (negative indices)
# Extract from index -7 to -3
print(sample_string[-7:-3])  # 'Worl'
print(sample_list[-7:-3])    # [30, 40, 50, 60]

# 3. Skipping elements (using step)
# Take every 2nd element from index 1 to 7
print(sample_string[1:8:2])  # 'el,W'
print(sample_list[1:8:2])    # [20, 40, 60, 80]

# 4. Reverse the entire string or list using slicing
print(sample_string[::-1])  # '!dlroW ,olleH'
print(sample_list[::-1])    # [90, 80, 70, 60, 50, 40, 30, 20, 10]

# 5. Omit start or end index
# From start to index 5:
print(sample_string[:5])  # 'Hello'
print(sample_list[:5])    # [10, 20, 30, 40, 50]

# From index 4 to end:
print(sample_string[4:])  # 'o, World!'
print(sample_list[4:])    # [50, 60, 70, 80, 90]

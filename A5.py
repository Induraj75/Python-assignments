# 1.	Write a Python program that iterates through integers from 1 to 50. For each multiple of 3, print "Fizz" for each multiple of 5, print "Buzz". For multiples of both 3 and 5, print "FizzBuzz" otherwise print the number itself.

for i in range(1,51):
            if i%3 == 0 and i%5 == 0:
                  print('Fizz Buzz')
            elif i%3 == 0:
                  print('Fizz')
            elif i%5 == 0:
                  print('Buzz')
            else:
                  print(i)


# output :
 
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# 16
# 17
# Fizz
# 19
# Buzz
# Fizz
# 22
# 23
# Fizz
# Buzz
# 26
# Fizz
# 28
# 29
# FizzBuzz
# 31
# 32
# Fizz
# 34
# Buzz
# Fizz
# 37
# 38
# Fizz
# Buzz
# 41
# Fizz
# 43
# 44
# FizzBuzz
# 46
# 47
# Fizz
# 49
# Buzz


# 2.	Create a multiplication table (1-10) using nested loops. include logic that if the result is over 50 you break out of the loop

for i in range(1, 11):
    for j in range(1, 11):
        result = i * j
        if result > 50:
            break 
        print(f"{i} x {j} = {result}")
    print() 

# output :
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# 1 x 4 = 4
# 1 x 5 = 5
# 1 x 6 = 6
# 1 x 7 = 7
# 1 x 8 = 8
# 1 x 9 = 9
# 1 x 10 = 10

# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 2 x 4 = 8
# 2 x 5 = 10
# 2 x 6 = 12
# 2 x 7 = 14
# 2 x 8 = 16
# 2 x 9 = 18
# 2 x 10 = 20

# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# 3 x 4 = 12
# 3 x 5 = 15
# 3 x 6 = 18
# 3 x 7 = 21
# 3 x 8 = 24
# 3 x 9 = 27
# 3 x 10 = 30

# 4 x 1 = 4
# 4 x 2 = 8
# 4 x 3 = 12
# 4 x 4 = 16
# 4 x 5 = 20
# 4 x 6 = 24
# 4 x 7 = 28
# 4 x 8 = 32
# 4 x 9 = 36
# 4 x 10 = 40

# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50

# 6 x 1 = 6
# 6 x 2 = 12
# 6 x 3 = 18
# 6 x 4 = 24
# 6 x 5 = 30
# 6 x 6 = 36
# 6 x 7 = 42
# 6 x 8 = 48

# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49

# 8 x 1 = 8
# 8 x 2 = 16
# 8 x 3 = 24
# 8 x 4 = 32
# 8 x 5 = 40
# 8 x 6 = 48

# 9 x 1 = 9
# 9 x 2 = 18
# 9 x 3 = 27
# 9 x 4 = 36
# 9 x 5 = 45

# 10 x 1 = 10
# 10 x 2 = 20
# 10 x 3 = 30
# 10 x 4 = 40
# 10 x 5 = 50


# 3.	Create a list of 10 numbers. Demonstrate various list methods (append, Insert, pop, remove ,sort ,etc). Show iteration that print only even numbers.
                     
    numbers = [20, 3, 15, 8, 12, 7, 5, 10, 2, 1]
#  append() - add 25 at the end
numbers.append(25)
print("After append(25):", numbers)       
# Output: After append(25): [20, 3, 15, 8, 12, 7, 5, 10, 2, 1, 25]


#  insert() - insert 30 at index 4
numbers.insert(4, 30)
print("After insert(4, 30):", numbers)
#  Output: After insert(4, 30): [20, 3, 15, 8, 30, 12, 7, 5, 10, 2, 1, 25]


# pop() - remove last item
popped = numbers.pop()
print("After pop():", numbers)
print("Popped item:", popped)
# Output:After pop(): [20, 3, 15, 8, 30, 12, 7, 5, 10, 2, 1]
# Popped item: 25


#  remove() - remove first occurrence of 30
numbers.remove(30)
print("After remove(30):", numbers)
#  Output: After remove(30): [20, 3, 15, 8, 12, 7, 5, 10, 2, 1]
 
 
#  sort() - sort the list ascending
numbers.sort()
print("After sort():", numbers)
# Output: After sort(): [1, 2, 3, 5, 7, 8, 10, 12, 15, 20]


# reverse() - reverse the list
numbers.reverse()
print("After reverse():", numbers)
# Output: After reverse(): [20, 15, 12, 10, 8, 7, 5, 3, 2, 1]


# Iterate and print even numbers only
print("Even numbers in the list:")
for num in numbers:
     if num % 2 == 0:
       print(num)

# Output : Even numbers in the list:
# 20
# 12
# 10
# 8
# 2


# 4. Create variable of each "advanced" data type (list, tuple, set, etc.). print each with a label describing the data type.

# 1.	List - ordered, mutable, allows duplicates
my_list = [1, 2, 3, 4, 5]
print("List:", my_list)

# output :-  List: [1, 2, 3, 4, 5]

# 2.	 Tuple - ordered, immutable, allows duplicates
my_tuple = (10, 20, 30, 40)
print("Tuple:", my_tuple)

# output :-  Tuple: (10, 20, 30, 40)

# 3.	 Set - unordered, mutable, no duplicates
my_set = {1, 2, 3, 3, 4}
print("Set:", my_set)

# output :-  Set: {1, 2, 3, 4}

# 4.	 Dictionary - unordered (Python 3.6+ maintains insertion order), mutable, key-value pairs
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print("Dictionary:", my_dict)
    
# output :-  Dictionary: {'name': 'Alice', 'age': 30, 'city': 'New York'}

# 5.	 Frozenset - immutable version of a set
my_frozenset = frozenset([5, 6, 7, 7, 8])
print("Frozenset:", my_frozenset)
      
# output :- Frozenset: frozenset({5, 6, 7, 8})

# 6.	 Byte - immutable sequence of bytes
my_bytes = bytes([65, 66, 67])
print("Bytes:", my_bytes)

# output :- Bytes: b'ABC'

# 7.	 Bytearray - mutable sequence of bytes
my_bytearray = bytearray([68, 69, 70])
print("Bytearray:", my_bytearray)

# output :- Bytearray: bytearray(b'DEF')

# 8.	 Range - immutable sequence of numbers
my_range = range(1, 6)
print("Range:", list(my_range))  
# Converted to list for display
# output :- Range: [1, 2, 3, 4, 5]

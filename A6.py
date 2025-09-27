# 1.	Show how immutability works by attempting to modify a tuple. Show the same with a list.

# Tuples are immutable cannot change elements of a tuple after it’s created.
my_tuple = (1, 2, 3)
            # Try to modify the first element
try:
    my_tuple[0] = 10
except TypeError as e:
    print("Tuple error:", e)

# output :- Tuple error: 'tuple' object does not support item assignment
# Lists are mutable can change elements of a list after it’s created.
                      
my_list = [1, 2, 3]
# Modify the first element
my_list[0] = 10
print("Modified list:", my_list)
                            
# output :- Modified list: [10, 2, 3]


# 2.	Create two sets of integers (with a few overlapping values).  Demonstrate union, intersection, difference, symmetric difference, etc.

A = {1, 2, 3, 4, 5, 6}
B = {4, 5, 6, 7, 8, 9}
        #    These sets have the overlapping values 4, 5, 6

c = A .union (B)            #  A|B
print(c)
# All unique elements from both sets.
# A ∪ B = {1,2,3,4,5,6,7,8,9}

c1 = A .intersection (B)        # A & B
print(c1)
    #   Only elements that are in both sets.
# A ∩ B = {4,5,6} 

c2= (A - B)           # A.difference(B)
print(c2)
# Elements in A that are not in B.
# A − B = {1,2,3} 

# Difference 
c3 = (B - A)          # B.difference(A)
print(c3)
# Elements in B that are not in A.
# B − A = {7,8,9} 

# Symmetric Difference 
c4 = A ^ B              # A.symmetric_difference(B)
print(c4)
# Elements in either A or B, but not in both.
# A △ B = {1,2,3,7,8,9} 

            #   Is A a subset of B? → No
            #   Is A a superset of B? → No
            #   Is {4, 5} a subset of A? → Yes


# 3.	Create a dictionary of student names as keys and their ages as values. Update, delete, and iterate over the dictionary to display items in a formatted manner (e.g., “Name → Age”).
       
students = {
    "Alice": 20,
    "Bob": 22,
    "Charlie": 19,
    "Diana": 21
}
        # Update a value
students["Charlie"] = 20
        # Add a new student
students["Ethan"] = 23
       # Delete a student
del students["Bob"]
      # Iterate and display
for name, age in students.items():
            print(f"{name} → {age}")  

# output :-                 
# Alice → 20
# Charlie → 20
# Diana → 21
# Ethan → 23


# 4. Convert a set into a frozenset. Attempt modifications to prove frozenset immutability.

my_set = {1, 2, 3}
             # Convert it to a frozenset
my_frozenset = frozenset(my_set)
print("Frozenset:", my_frozenset)         
                 
# output :-
# Frozenset: frozenset({1, 2, 3})
        # Attempt to add an element
# my_frozenset.add(4)             # AttributeError
      # Attempt to remove an element 
# my_frozenset.remove(2)       # AttributeError

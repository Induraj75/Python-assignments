# 1.	write a function that demonstrates required, default, and keyword arguments.  call it multiple ways to show how parameter passing differs.

def describe_pet(pet_name, animal_type='dog', age=None):
    print(f"\nPet Info:")
    print(f"Animal Type: {animal_type}")
    print(f"Pet Name: {pet_name}")
    if age is not None:
        print(f"Age: {age}")
    else:
        print("Age: Unknown")
# 1. Only required argument (uses defaults for others)
describe_pet('Buddy')

# output :-    
# Pet Info:
# Animal Type: dog
# Pet Name: Buddy
# Age: Unknown

# 2. Required + one default override
describe_pet('Whiskers', 'cat')
# output :-    
# Pet Info:
# Animal Type: cat
# Pet Name: Whiskers
# Age: Unknown

# 3. All positional arguments
describe_pet('Goldie', 'fish', 1)
# output :-    
# Pet Info:
# Animal Type: fish
# Pet Name: Goldie
# Age: 1

# 4. Using keyword arguments for flexibility
describe_pet(pet_name='Rex', age=5)
# output :-    
# Pet Info:
# Animal Type: dog
# Pet Name: Rex
# Age: 5

# 5. Mixing positional and keyword (positional first)
describe_pet('Bella', age=2)       
# output :-    
# Pet Info:
# Animal Type: dog
# Pet Name: Bella
# Age: 2

# 6. All keyword arguments (order doesn't matter)
describe_pet(age=3, pet_name='Charlie', animal_type='parrot')
# output :-    
# Pet Info:
# Animal Type: parrot
# Pet Name: Charlie
# Age: 3

# 2.  Create a list of integers. Use a lambda and map() to square each integer. Print the resulting list.
               
numbers = [1, 2, 3, 4, 5]
    # Use map and lambda to square each integer
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)

# output :- [1, 4, 9, 16, 25]

# 3.  Prompt the user for a sentence. Split the sentence into words and print each word on a new line with its length.
                
sentence = input("Enter a sentence: ")
                     # Split the sentence into words
words = sentence.split()
                    # Print each word with its length
for word in words:
      print(f"{word} ({len(word)})")

# output :-
# Enter a sentence: Python is awesome
# Python (6)
# is (2)
# awesome (7)

# 4.  Use the format() method or f-Strings to output a descriptive message about yourself (name, age, hobby).

# Using format() method:
name = "Alex"
age = 25
hobby = "playing guitar"
message = "Hi, I'm {}. I'm {} years old and I enjoy {}.".format(name, age, hobby)
print(message)

# output :-
# Hi, I'm Alex. I'm 25 years old and I enjoy playing guitar.

# Using f-Strings :
name = "Alex"
age = 25
hobby = "playing guitar"
message = f"Hi, I'm {name}. I'm {age} years old and I   enjoy {hobby}."
print(message)

# output :-
# Hi, I'm Alex. I'm 25 years old and I enjoy playing guitar.

# 1. Create a text file with a few lines of data. Write a Python script that reads the file, counts the words, and outputs the result. Write the word count result to a new file.

# Hello world.
# This is a simple text file.
# It contains several words.
# Let’s count them!                   
          # Save this as sample.txt
    #  Python script to count words and write to a new file        
def count_words_in_file(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            text = file.read()
            words = text.split()
            word_count = len(words)
        with open(output_file, 'w') as result_file:
            result_file.write(f"Word count: {word_count}\n")
        print(f"Word count written to '{output_file}'")
    except FileNotFoundError:
        print(f"The file '{input_file}' does not exist.")

# Usage
input_filename = 'sample.txt'
output_filename = 'word_count_result.txt'
count_words_in_file(input_filename, output_filename)

# output :-
# Word count written to 'word_count_result.txt'
# Word count: 15


# 2. Write a function that attempts to convert a user’s input to an integer.  Use try-except to catch ValueError. Print a custom message if input is invalid.

def get_integer_from_user():
    user_input = input("Please enter an integer: ")
    try:
        value = int(user_input)
        print(f"You entered the integer: {value}")
        return value
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        return None

get_integer_from_user()

# output :-  
# valid :- Please enter an integer: 42
# You entered the integer: 42

# Invalid :- Please enter an integer: hello
# Invalid input! Please enter a valid integer.

# 3. Write a Python script that reads a file and finds all occurrences of a valid email format using regex. Print the extracted emails.

import re
def extract_emails(filename):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    with open(filename, 'r') as file:
        content = file.read()
        emails = re.findall(email_pattern, content)
        for email in emails:
           print(email)
        if __name__ == "__main__":
             filename = "sample.txt"
             extract_emails(filename) 

        # Create a file called sample.txt with some text including emails, for example:
            #   Hello,
            #  Please contact us at support@example.com or            sales@example.co.uk.
            # Also, reach out to admin123@my-domain.org for more info.
            # Thank you!

# output :-      
# support@example.com
# sales@example.co.uk
# admin123@my-domain.org 
    
# 4. Create a Vehicle class with attributes like make, model, and a method start_engine().  Create a subclass Car that inherits from Vehicle and overrides start_engine() with a custom message.

    class Vehicle:
        def __init__(self, make, model):
            self.make = make
            self.model = model

        def start_engine(self):
            print(f"The engine of the {self.make} {self.model} is starting.")

    class Car(Vehicle):
        def start_engine(self):
            print(f"The car {self.make} {self.model} engine roars to life!")

    vehicle = Vehicle("GenericMake", "GenericModel")
    vehicle.start_engine()

    car = Car("Toyota", "Corolla")
    car.start_engine()
                            
# output :-
# The engine of the GenericMake GenericModel is starting.
# The car Toyota Corolla engine roars to life!

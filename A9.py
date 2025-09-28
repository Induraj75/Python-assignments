# create a basic Tkinter window with a label saying "Welcome to my first GuI!" Add a button that when clicked, changes the label text.

import tkinter as tk

def change_text():
    label.config(text="Button Clicked! Hello, Tkinter!")

# Create the main window
root = tk.Tk()
root.title("My First GUI")
root.geometry("300x150")  # Set window size

# Create a label
label = tk.Label(root, text="Welcome to my first GUI!", font=("Arial", 14))
label.pack(pady=20)

# Create a button
button = tk.Button(root, text="Click Me", command=change_text)
button.pack()

# Run the application
root.mainloop()


# 2. Create two frames in a Tkinter window. Experiment with pack() and grid() layout managers to arrange widgets take screenshots or note your observations 

import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Tkinter Layout Experiment")
root.geometry("400x300")

# Create two frames
frame1 = tk.Frame(root, bg="lightblue", width=200, height=300)
frame2 = tk.Frame(root, bg="lightgreen", width=200, height=300)

# Use pack() to place the frames side by side
frame1.pack(side="left", fill="both", expand=True)
frame2.pack(side="right", fill="both", expand=True)

# --- Adding widgets using grid() in frame1 ---
label1 = tk.Label(frame1, text="Frame 1 - Grid Layout", bg="lightblue")
btn1 = tk.Button(frame1, text="Button 1")
btn2 = tk.Button(frame1, text="Button 2")

label1.grid(row=0, column=0, columnspan=2, pady=10)
btn1.grid(row=1, column=0, padx=10, pady=10)
btn2.grid(row=1, column=1, padx=10, pady=10)

# --- Adding widgets using pack() in frame2 ---
label2 = tk.Label(frame2, text="Frame 2 - Pack Layout", bg="lightgreen")
btn3 = tk.Button(frame2, text="Button 3")
btn4 = tk.Button(frame2, text="Button 4")

label2.pack(pady=10)
btn3.pack(pady=5)
btn4.pack(pady=5)

# Start main loop
root.mainloop()

# Frame1 (using grid()):
# Widgets are arranged in a grid (row/column format).
# You have precise control over placement (e.g., row=1, column=0).
# Useful when you need a table-like structure.

# Frame2 (using pack()):
# Widgets are stacked vertically by default (side="top" is default).
# Easier for linear layouts but less flexible.
# Adding padding (padx, pady) helps with spacing.

# Important Notes:
# You should not mix pack() and grid() in the same container (frame).
# This can lead to TclError or unexpected behavior.
# But you can use pack() in one frame and grid() in another


# 3. create a 2D Numpy array (size 3x3). print its shape,size, and data type. calculate row-wise and column-wise sums.

import numpy as np

# Create a 3x3 numpy array
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Print shape, size, and data type
print("Array:\n", arr)
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Data Type:", arr.dtype)

# Row-wise sum (sum along axis=1)
row_sum = np.sum(arr, axis=1)
print("Row-wise sum:", row_sum)

# Column-wise sum (sum along axis=0)
col_sum = np.sum(arr, axis=0)
print("Column-wise sum:", col_sum)


# output :-
# Array:
#  [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
# Shape: (3, 3)
# Size: 9
# Data Type: int64
# Row-wise sum: [ 6 15 24]
# Column-wise sum: [12 15 18]


# 4. create a 1D Numpy array with 12 elements(0-11). reshape it to 3x4. Multiply all elements by 2 and find the standard deviation 

import numpy as np
# Step 1: Create 1D array
arr = np.arange(12)                        
# [ 0  1  2  3  4  5  6  7  8  9 10 11]

# Step 2: Reshape to 3x4
reshaped_arr = arr.reshape((3, 4))                  
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# Step 3: Multiply all elements by 2
multiplied_arr = reshaped_arr * 2
# [[ 0  2  4  6]
#  [ 8 10 12 14]
#  [16 18 20 22]]

# Step 4: Find standard deviation
std_dev = np.std(multiplied_arr)
print("Array:\n", multiplied_arr)
print("Standard Deviation:", std_dev)
#  6.9041

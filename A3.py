# 1. Open the same Python script in both Jupyter Notebook and Spyder. Compare the user experience, features (like variable explorer, cell execution, inline plots), and note any differences
 
# 1. Interface & User Experience
    #    Jupyter Notebook
# Interface: Web-based (runs in browser).
# Script Format: .ipynb (not standard .py) using code "cells".
# Cell Execution: Code is run cell-by-cell interactively.
# Inline Output: Output, plots, and markdown are rendered directly below each cell.
# Notebook-style: Good for exploratory analysis, documentation, and presentation.

# Spyder
    # Interface: Desktop IDE similar to MATLAB.
# Script Format: Uses .py files by default (you can also use IPython console).
# Execution: Can run full scripts or selected code blocks (with F9, F5, etc.).
# Inline Output: Supports inline plotting in the IPython console.
# IDE-style: Better suited for structured coding, debugging, and larger projects.

# 2. Variable Explorer
          # Jupyter Notebook
# No native variable explorer by default.
# Can be added with extensions (like JupyterLab + variable inspector), but not as robust.
# Variables must be printed manually or via %who, %whos.

# Spyder
# Excellent variable explorer out of the box.
# Displays all user-defined variables with types, sizes, and values.
# Allows interactive inspection and editing of DataFrames, arrays, etc.

# 3. Cell Execution & Workflow
      # Jupyter Notebook
# Code is divided into cells.
# You can run a single cell (Shift + Enter) or groups.
# Keeps execution state even when jumping between cells (can cause confusion).
# Easy to interleave code with markdown and visualizations.

# Spyder
# You can simulate cell execution by using # %% to define code cells in .py files.
# Run selected cells with Shift+Enter or Ctrl+Enter.
# Execution is more linear and resembles how scripts are normally run.
# More suited for script-style development.

# 4. Plotting & Visualization
    #   Jupyter Notebook
# Plots appear inline below each cell.
# Very good for step-by-step data visualization.
# Good support for interactive widgets via ipywidgets.

# Spyder
# Plots appear in a dedicated Plots pane or inline (configurable).
# Can be saved, browsed, or cleared separately.
# Good support for Matplotlib, Seaborn, etc.

# 5. Debugging Tools
    #   Jupyter Notebook
# Very basic debugging (via print() or %debug magic).
# Some limited interactive debugging in JupyterLab.
# Less intuitive for tracing complex logic.

# Spyder
# Full-featured debugger with breakpoints, step-in/out, and variable inspection.
# Easy to trace bugs in long scripts.
# Better suited for software development or debugging complex logic.

# 6. Documentation & Help
# Jupyter Notebook
# Excellent for tutorials, educational content, or data storytelling.
# Supports markdown, LaTeX, and embedded visualizations.
# Easily shared via .ipynb files or platforms like NBViewer, GitHub, or JupyterHub.

# Spyder
# Built-in help pane, integrates with Docstrings.
# Hovering shows tooltips/documentation.
# More IDE-like experience for developers.

# 7. Performance & Resources
# Jupyter Notebook
# Runs in browser, backend (kernel) can crash on large workloads.
# Not ideal for very long scripts or memory-heavy processes.

# Spyder
# More robust for longer scripts or larger data handling.
# Still memory-intensive, but more stable for complex projects.

# 2. Verify that your PATH variable is set correctly for Python (or Anaconda). Write instructions (like a mini-how-to-guide) for a newcomer to set environment variables on window or linux

# PATH Variable :-
# The PATH is an environment variable that tells your system where to look for executable files like python or conda. If Python or Anaconda isn't in your PATH, you'll get errors like:
# 'python' is not recognized as an internal or external command

# Windows: Setting PATH for Python or Anaconda
# Step 1: Check if Python/Anaconda is already in PATH
# Open Command Prompt (cmd).
# Type:
# python --version
# or
# conda --version

# Step 2: Find the installation path
# Python: Typically installed in:
# C:\Users\<YourUsername>\AppData\Local\Programs\Python\Python3X\
# Anaconda: Usually in:
# C:\Users\<YourUsername>\Anaconda3\

# Step 3: Add to PATH manually
# Press Windows Key → search for "Environment Variables" → Click:
# Edit the system environment variables
# Then click on "Environment Variables..."
# In the System variables or User variables section:
# Find the variable named Path, select it, and click Edit.
# Click New and paste in the path to your Python or Anaconda folder, e.g.:
# C:\Users\<YourUsername>\AppData\Local\Programs\Python\Python3X\
# Also add the Scripts folder:
# C:\Users\<YourUsername>\AppData\Local\Programs\Python\Python3X\Scripts\
# Click OK → OK → OK.
# Restart your Command Prompt and type:
# python --version

# Linux: Setting PATH for Python or Anaconda
# Step 1: Check if Python/Anaconda is already in PATH
# Open a terminal and type:
# python3 --version

# Step 2: Find where Python or Anaconda is installed
# Python is often installed by default.
# Run which python3 to find its path.
# Anaconda is usually in your home directory:
# ~/anaconda3/

# Step 3: Add to PATH in .bashrc or .zshrc
# Open your shell config file in a text editor:
# nano ~/.bashrc
# Or for Zsh users:
# nano ~/.zshrc
# Add the following line at the end of the file:
# export PATH="$HOME/anaconda3/bin:$PATH"
# Or if you're adding Python manually (replace with your actual path):
# export PATH="/usr/local/bin/python3.11:$PATH"
# Save and exit (Ctrl + O, Enter, then Ctrl + X).
# Reload your shell:
# source ~/.bashrc
# Test:
# python3 --version


# 3. create and print variables of all fundamental data types

# Integer
my_int = 42
print("Integer:", my_int)

# Float
my_float = 3.14
print("Float:", my_float)

# String
my_str = "Hello, world!"
print("String:", my_str)

# Boolean
my_bool = True
print("Boolean:", my_bool)

# NoneType
my_none = None
print("NoneType:", my_none)

# List
my_list = [1, 2, 3, "apple"]
print("List:", my_list)

# Tuple
my_tuple = (10, 20, 30)
print("Tuple:", my_tuple)

# Set
my_set = {1, 2, 3}
print("Set:", my_set)

# Dictionary
my_dict = {"name": "Alice", "age": 25}
print("Dictionary:", my_dict)

# output
# Integer: 42
# Float: 3.14
# String: Hello, world!
# Boolean: True
# NoneType: None
# List: [1, 2, 3, 'apple']
# Tuple: (10, 20, 30)
# Set: {1, 2, 3}
# Dictionary: {'name': 'Alice', 'age': 25}


# 4. convert a single integer into binary, octal and hex, and print the results

# Original integer
num = 42

# Convert to different bases
binary = bin(num)     # Binary representation
octal = oct(num)      # Octal representation
hexadecimal = hex(num)  # Hexadecimal representation

# Print the results
print("Original integer:", num)
print("Binary:", binary)
print("Octal:", octal)
print("Hexadecimal:", hexadecimal)

# output
# Original integer: 42
# Binary: 0b101010
# Octal: 0o52
# Hexadecimal: 0x2a


# 5. Demonstrate the difference between a mutable type (e.g., list) and an immutable type (e.g., string or tuple) by attempting to change their values in a python script. Report what happens

# Mutable Type: List
my_list = [1, 2, 3]
print("Original list:", my_list)

# Modify an element
my_list[0] = 99
print("Modified list:", my_list)  # This will work!

# Immutable Type: String
my_string = "hello"
print("Original string:", my_string)

try:
    # Try to change the first character of the string
    my_string[0] = "H"
except TypeError as e:
    print("Error when modifying string:", e)

# Immutable Type: Tuple
my_tuple = (10, 20, 30)
print("Original tuple:", my_tuple)

try:
    # Try to change an element in the tuple
    my_tuple[1] = 200
except TypeError as e:
    print("Error when modifying tuple:", e)

# output
# Original list: [1, 2, 3]
# Modified list: [99, 2, 3]
# Original string: hello
# Error when modifying string: 'str' object does not support item assignment
# Original tuple: (10, 20, 30)
# Error when modifying tuple: 'tuple' object does not support item assignment

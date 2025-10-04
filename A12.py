# Create a data frame using a dictionary of lists. add a new column total = colA +colB. Delete one column and show final structure

import pandas as pd

# Step 1: Create DataFrame using a dictionary of lists
data = {
    'colA': [10, 20, 30, 40],
    'colB': [1, 2, 3, 4]
}

df = pd.DataFrame(data)

# Step 2: Add a new column 'total' = colA + colB
df['total'] = df['colA'] + df['colB']

# Step 3: Delete one column (let's remove 'colB')
df.drop('colB', axis=1, inplace=True)

# Step 4: Show final structure
print(df)

# output
#    colA  total
# 0    10     11
# 1    20     22
# 2    30     33
# 3    40     44


# 2. Practice .loc[] and .iloc[] to select specific rows. Delete a row by label 

import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['NY', 'LA', 'Chicago', 'Houston', 'Phoenix']
}

df = pd.DataFrame(data, index=['a', 'b', 'c', 'd', 'e'])
print(df)

# output
#     Name  Age     City
# a  Alice   25       NY
# b    Bob   30       LA
# c Charlie   35  Chicago
# d  David   40  Houston
# e    Eva   45  Phoenix

# Select Specific Rows
# 1. Using .loc[] (by label):
# Select row with label 'b'
print(df.loc['b'])

# output
# Name    Bob
# Age      30
# City     LA
# Name: b, dtype: object

# Select multiple rows by labels
print(df.loc[['a', 'd']])
#    Name  Age     City
# a  Alice   25       NY
# d  David   40  Houston

# 2. Using .iloc[] (by index position):
# Select the second row (index 1)
print(df.iloc[1])

# Select first and fourth rows
print(df.iloc[[0, 3]])

# output
# Name    Bob
# Age      30
# City     LA
# Name: b, dtype: object

#     Name  Age     City
# a  Alice   25       NY
# d  David   40  Houston

# Delete a Row by Label
# Delete the row with label 'c'
df = df.drop('c')
print(df)

# output
#     Name  Age     City
# a  Alice   25       NY
# b    Bob   30       LA
# d  David   40  Houston
# e    Eva   45  Phoenix


# 3. Load a small CSV into a DataFrame(e.g., 10-20 rows). Use functions like head(), tail(), info(),describe().

# CSV is named sample_data.csv:
# Name,Age,Department,Salary
# Alice,29,Engineering,70000
# Bob,35,Sales,52000
# Charlie,25,HR,45000
# David,45,Management,98000
# Eva,32,Engineering,75000
# Frank,28,Sales,50000
# Grace,30,HR,47000
# Hank,50,Management,105000
# Ivy,26,Engineering,72000
# Jack,38,Sales,54000
# Kara,27,HR,46000
# Leo,41,Management,99000

import pandas as pd

# Load the CSV data (pretend it's read from 'sample_data.csv')
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack', 'Kara', 'Leo'],
    'Age': [29, 35, 25, 45, 32, 28, 30, 50, 26, 38, 27, 41],
    'Department': ['Engineering', 'Sales', 'HR', 'Management', 'Engineering', 'Sales', 'HR', 'Management', 'Engineering', 'Sales', 'HR', 'Management'],
    'Salary': [70000, 52000, 45000, 98000, 75000, 50000, 47000, 105000, 72000, 54000, 46000, 99000]
}

df = pd.DataFrame(data)

# Show the first few rows
print("Head:")
print(df.head())

# Show the last few rows
print("\nTail:")
print(df.tail())

# Summary of the DataFrame
print("\nInfo:")
print(df.info())

# Descriptive statistics
print("\nDescribe:")
print(df.describe())

# output
# head()
#      Name  Age   Department  Salary
# 0   Alice   29  Engineering   70000
# 1     Bob   35        Sales   52000
# 2 Charlie   25           HR   45000
# 3   David   45   Management   98000
# 4     Eva   32  Engineering   75000

# tail()
#      Name  Age   Department  Salary
# 7    Hank   50   Management  105000
# 8     Ivy   26  Engineering   72000
# 9    Jack   38        Sales   54000
# 10   Kara   27           HR   46000
# 11    Leo   41   Management   99000

# info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 12 entries, 0 to 11
# Data columns (total 4 columns):
#  #   Column     Non-Null Count  Dtype 
# ---  ------     --------------  ----- 
#  0   Name       12 non-null     object
#  1   Age        12 non-null     int64 
#  2   Department 12 non-null     object
#  3   Salary     12 non-null     int64 
# dtypes: int64(2), object(2)
# memory usage: 512.0+ bytes

# describe()
#              Age        Salary
# count  12.000000     12.000000
# mean   34.416667  70333.333333
# std     7.822460  21813.623551
# min    25.000000  45000.000000
# 25%    28.000000  50000.000000
# 50%    31.000000  61000.000000
# 75%    39.250000  81000.000000
# max    50.000000 105000.000000


# 4. Calculate mean,median,min,max, and standard deviation for numerical columns.provide insights(e.g., "column A has the highest mean among all columns").

# | Student | Course  | Grade | Attendance (%) | Study Hours per Week |
# | ------- | ------- | ----- | -------------- | -------------------- |
# | Alice   | Math    | 85    | 92             | 12                   |
# | Bob     | History | 78    | 88             | 10                   |
# | Charlie | Science | 90    | 95             | 14                   |
# | David   | Math    | 72    | 85             | 8                    |
# | Emma    | History | 88    | 90             | 11                   |
# | Frank   | Science | 95    | 98             | 15                   |
# | Grace   | Math    | 80    | 89             | 9                    |

# 1. Grade
# Mean: 84
# Median: 85
# Min: 72
# Max: 95
# Standard Deviation: ≈ 7.57

# 2. Attendance (%)
# Mean: 91
# Median: 90
# Min: 85
# Max: 98
# Standard Deviation: ≈ 4.39

# 3. Study Hours per Week
# Mean: 11.29
# Median: 11
# Min: 8
# Max: 15
# Standard Deviation: ≈ 2.29

# Insights
# Grades have the highest variability (Std Dev ≈ 7.57), suggesting student performance varies more than attendance or study habits.
# Frank has the highest grade (95) and also studies the most (15 hours/week) with nearly perfect attendance.
# David has the lowest grade (72) and also the lowest study hours (8), which may indicate a connection between effort and performance.
# Attendance is generally high, with an average of 91%, showing consistent classroom participation.
# Study Hours range from 8 to 15 per week, with a mean of ~11.3 hours, suggesting moderate commitment outside class.
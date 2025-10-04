# 1. Create two small DataFrames that share a common key (e.g., "id"). Merge them with different join types(inner,outer,left,right) and show results.

import pandas as pd

# Create DataFrame A
df_a = pd.DataFrame({
    'id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie']
})

# Create DataFrame B
df_b = pd.DataFrame({
    'id': [2, 3, 4],
    'age': [30, 25, 40]
})

# Inner Join
inner_join = pd.merge(df_a, df_b, on='id', how='inner')

# Outer Join
outer_join = pd.merge(df_a, df_b, on='id', how='outer')

# Left Join
left_join = pd.merge(df_a, df_b, on='id', how='left')

# Right Join
right_join = pd.merge(df_a, df_b, on='id', how='right')

# Show results
print("DataFrame A:")
print(df_a)
print("\nDataFrame B:")
print(df_b)

print("\nInner Join:")
print(inner_join)

print("\nOuter Join:")
print(outer_join)

print("\nLeft Join:")
print(left_join)

print("\nRight Join:")
print(right_join)


# output
# DataFrame A
#    id    name
# 0   1   Alice
# 1   2     Bob
# 2   3  Charlie

# DataFrame B
#    id  age
# 0   2   30
# 1   3   25
# 2   4   40

# Inner Join (only matching ids)
#    id    name  age
# 0   2     Bob   30
# 1   3  Charlie   25

# Outer Join (all rows, matching where possible)
#    id    name   age
# 0   1   Alice   NaN
# 1   2     Bob  30.0
# 2   3  Charlie 25.0
# 3   4     NaN  40.0

# Left Join (all from A, matched from B)
#    id    name   age
# 0   1   Alice   NaN
# 1   2     Bob  30.0
# 2   3  Charlie 25.0

# Right Join (all from B, matched from A)
#    id    name  age
# 0   2     Bob   30
# 1   3  Charlie   25
# 2   4     NaN   40


# 2. Load a dataset(e.g., a small csv of sales data with columns like region, sales). Group data by region and compute total sales. plot a bar chart of total sales per region.

# region,sales
# North,1200
# South,1500
# East,1000
# West,1700
# North,1100
# South,1300
# East,900
# West,1600

import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

# Sample CSV data
csv_data = """
region,sales
North,1200
South,1500
East,1000
West,1700
North,1100
South,1300
East,900
West,1600
"""

# Read the CSV data into a DataFrame
df = pd.read_csv(StringIO(csv_data))

# Group by 'region' and compute total sales
grouped = df.groupby('region')['sales'].sum().reset_index()

# Plotting
plt.figure(figsize=(8, 6))
plt.bar(grouped['region'], grouped['sales'], color='skyblue')
plt.title('Total Sales per Region')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


# 3. Read data from a URL (e.g., pd.read_html of a public website table). convert it to a CSV file.

import pandas as pd
# Step 1: Specify the URL
url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"  # Example URL with tables

# Step 2: Read all tables on the page
tables = pd.read_html(url)

# Step 3: Select the table you want
# Let's pick the first table as an example
df = tables[0]

# Step 4: Save it to a CSV file
df.to_csv("gdp_by_country.csv", index=False)
print("CSV file saved successfully.")


# 4.  Copy some tabular data from a spreadsheet into your clipboard. use pd.read_clipboard() to create a dataframe. perform a minor transformation(like sorting) and then write it to an excel file

# Name    Age    Score
# Alice   25     85
# Bob     30     90
# Charlie 22     88

import pandas as pd

# Step 1: Read the copied data from clipboard
df = pd.read_clipboard()

# Step 2: Minor transformation - sort by 'Score' descending
df_sorted = df.sort_values(by='Score', ascending=False)

# Step 3: Write the sorted DataFrame to an Excel file
df_sorted.to_excel("sorted_output.xlsx", index=False)

print("Data sorted and saved to 'sorted_output.xlsx'")

# Ensure the column headers are present when copying the data.
# pd.read_clipboard() works only in local environments with clipboard access.
# The output Excel file (sorted_output.xlsx) will be saved in your current working directory.
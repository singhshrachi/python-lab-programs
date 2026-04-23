# Q28. Program using pandas to read a CSV file and perform basic analysis.

import pandas as pd

# Create a sample CSV file
csv_data = """Name,Age,Course,Marks,City
Rahul,20,BCA,85.5,Sagar
Priya,21,BCA,90.0,Bhopal
Amit,22,MCA,78.0,Indore
Sneha,20,BCA,92.5,Sagar
Vivek,23,MCA,88.0,Bhopal
Neha,21,BCA,75.0,Indore
Ravi,22,MCA,95.0,Sagar
Pooja,20,BCA,82.0,Bhopal
Karan,21,MCA,70.0,Indore
Anita,22,BCA,88.5,Sagar
"""

with open("students.csv", "w") as f:
    f.write(csv_data)

print("'students.csv' created successfully.\n")

# Read CSV
df = pd.read_csv("students.csv")

print("=== First 5 Rows (head) ===")
print(df.head())

print("\n=== Last 3 Rows (tail) ===")
print(df.tail(3))

print(f"\n=== Shape ===\nRows: {df.shape[0]}, Columns: {df.shape[1]}")

print(f"\n=== Column Names ===\n{list(df.columns)}")

print(f"\n=== Data Types ===\n{df.dtypes}")

print(f"\n=== Basic Statistics ===")
print(df.describe())

print(f"\n=== Missing Values ===\n{df.isnull().sum()}")

print(f"\n=== Value Counts (Course) ===")
print(df["Course"].value_counts())

print(f"\n=== Average Marks : {df['Marks'].mean():.2f} ===")
print(f"Max Marks : {df['Marks'].max()}")
print(f"Min Marks : {df['Marks'].min()}")

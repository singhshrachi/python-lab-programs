# Q29. Program using pandas to filter and group data.

import pandas as pd

# Create sample data
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

df = pd.read_csv("students.csv")

# --- Filtering ---
print("=== Filtering ===\n")

print("Students with Marks > 85:")
print(df[df["Marks"] > 85])

print("\nBCA students only:")
print(df[df["Course"] == "BCA"])

print("\nStudents from Sagar:")
print(df[df["City"] == "Sagar"])

print("\nBCA students from Sagar with Marks > 85 (multiple conditions):")
print(df[(df["Course"] == "BCA") & (df["City"] == "Sagar") & (df["Marks"] > 85)])

# --- Groupby ---
print("\n=== Groupby ===\n")

print("Average Marks by Course:")
print(df.groupby("Course")["Marks"].mean())

print("\nStudent Count by City:")
print(df.groupby("City")["Name"].count())

print("\nMax Marks by Course:")
print(df.groupby("Course")["Marks"].max())

print("\nMultiple aggregations by Course:")
print(df.groupby("Course")["Marks"].agg(["mean", "max", "min", "count"]))

# --- Sorting ---
print("\n=== Sorting ===\n")

print("Top 3 students by Marks:")
print(df.nlargest(3, "Marks")[["Name", "Course", "Marks"]])

print("\nBottom 3 students by Marks:")
print(df.nsmallest(3, "Marks")[["Name", "Course", "Marks"]])

print("\nSorted by Name alphabetically:")
print(df.sort_values("Name")[["Name", "Marks"]].reset_index(drop=True))

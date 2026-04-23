# Q22. Program to perform INSERT, UPDATE, DELETE, and SELECT operations on a database.

import sqlite3

conn = sqlite3.connect("college.db")
cursor = conn.cursor()

# Create table fresh
cursor.execute("DROP TABLE IF EXISTS students")
cursor.execute("""
    CREATE TABLE students (
        id      INTEGER PRIMARY KEY AUTOINCREMENT,
        name    TEXT    NOT NULL,
        age     INTEGER NOT NULL,
        course  TEXT    NOT NULL,
        marks   REAL
    )
""")
conn.commit()

# --- INSERT ---
print("=" * 40)
print("INSERT Records")
print("=" * 40)

students = [
    ("Rahul",  20, "BCA", 85.5),
    ("Priya",  21, "BCA", 90.0),
    ("Amit",   22, "MCA", 78.0),
    ("Sneha",  20, "BCA", 92.5),
]
cursor.executemany(
    "INSERT INTO students (name, age, course, marks) VALUES (?, ?, ?, ?)",
    students
)
conn.commit()
print("4 records inserted successfully.")

# --- SELECT ---
print("\n" + "=" * 40)
print("SELECT All Records")
print("=" * 40)
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
print(f"{'ID':<5} {'Name':<10} {'Age':<5} {'Course':<8} {'Marks'}")
print("-" * 35)
for row in rows:
    print(f"{row[0]:<5} {row[1]:<10} {row[2]:<5} {row[3]:<8} {row[4]}")

# --- UPDATE ---
print("\n" + "=" * 40)
print("UPDATE Record")
print("=" * 40)
cursor.execute("UPDATE students SET marks = 95.0 WHERE name = 'Rahul'")
conn.commit()
print("Rahul's marks updated to 95.0")

cursor.execute("SELECT * FROM students WHERE name = 'Rahul'")
print(f"Updated: {cursor.fetchone()}")

# --- DELETE ---
print("\n" + "=" * 40)
print("DELETE Record")
print("=" * 40)
cursor.execute("DELETE FROM students WHERE name = 'Amit'")
conn.commit()
print("Amit's record deleted.")

cursor.execute("SELECT * FROM students")
print("\nRecords after delete:")
for row in cursor.fetchall():
    print(f"  {row}")

conn.close()
print("\nConnection closed.")

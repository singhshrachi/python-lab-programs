# Q23. Demonstrate transaction control (commit and rollback) in database operations.

import sqlite3

conn = sqlite3.connect("college.db")
cursor = conn.cursor()

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

# --- Transaction 1: Successful (commit) ---
print("=" * 45)
print("Transaction 1 - Successful (commit)")
print("=" * 45)
try:
    cursor.execute("INSERT INTO students (name, age, course, marks) VALUES (?, ?, ?, ?)",
                   ("Rahul", 20, "BCA", 85.5))
    cursor.execute("INSERT INTO students (name, age, course, marks) VALUES (?, ?, ?, ?)",
                   ("Priya", 21, "BCA", 90.0))
    conn.commit()
    print("Both records inserted and committed successfully.")
except Exception as e:
    conn.rollback()
    print(f"Error! Rolled back. {e}")

# --- Transaction 2: Failed (rollback) ---
print("\n" + "=" * 45)
print("Transaction 2 - Failed (rollback)")
print("=" * 45)
try:
    cursor.execute("INSERT INTO students (name, age, course, marks) VALUES (?, ?, ?, ?)",
                   ("Vivek", 22, "MCA", 88.0))
    print("Vivek's record inserted (not yet committed)...")
    raise Exception("Simulated error! Power failure or network issue.")
    conn.commit()
except Exception as e:
    conn.rollback()
    print(f"Error caught: {e}")
    print("Transaction rolled back! Vivek's record was NOT saved.")

# --- Final state ---
print("\n" + "=" * 45)
print("Final Records in Database")
print("=" * 45)
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()
for row in rows:
    print(f"  {row}")

conn.close()
print("\nConnection closed.")

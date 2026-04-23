# Q21. Program to connect to a database and create a table.

import sqlite3

# Connect to database (creates file if not exists)
conn = sqlite3.connect("college.db")
cursor = conn.cursor()

print("Connected to database 'college.db' successfully.")

# Drop table if already exists (for fresh run)
cursor.execute("DROP TABLE IF EXISTS students")

# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id      INTEGER PRIMARY KEY AUTOINCREMENT,
        name    TEXT    NOT NULL,
        age     INTEGER NOT NULL,
        course  TEXT    NOT NULL,
        marks   REAL
    )
""")

conn.commit()
print("Table 'students' created successfully.")

# Show table info
cursor.execute("PRAGMA table_info(students)")
columns = cursor.fetchall()
print("\nTable Structure:")
print(f"{'Col ID':<8} {'Name':<10} {'Type':<10} {'Not Null':<10} {'Primary Key'}")
print("-" * 50)
for col in columns:
    print(f"{col[0]:<8} {col[1]:<10} {col[2]:<10} {col[3]:<10} {col[5]}")

conn.close()
print("\nConnection closed.")

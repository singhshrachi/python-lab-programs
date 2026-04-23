# Q17. Program to read contents of a file using read(), readline(), and readlines().

# First, create a sample file
with open("sample.txt", "w") as f:
    f.write("Line 1: Hello, Python!\n")
    f.write("Line 2: File handling is easy.\n")
    f.write("Line 3: BCA Semester IV\n")
    f.write("Line 4: Python Programming Lab\n")

print("'sample.txt' created successfully.\n")

# --- read() - reads entire file as one string ---
print("=" * 40)
print("Using read():")
print("=" * 40)
with open("sample.txt", "r") as f:
    content = f.read()
    print(content)

# --- readline() - reads one line at a time ---
print("=" * 40)
print("Using readline():")
print("=" * 40)
with open("sample.txt", "r") as f:
    line = f.readline()
    while line:
        print(line, end="")
        line = f.readline()

# --- readlines() - reads all lines into a list ---
print("\n" + "=" * 40)
print("Using readlines():")
print("=" * 40)
with open("sample.txt", "r") as f:
    lines = f.readlines()
    print(f"Total lines: {len(lines)}")
    for i, line in enumerate(lines, 1):
        print(f"  Line {i}: {line}", end="")

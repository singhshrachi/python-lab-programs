# Q18. Program to write and append data to a file.

# --- Write mode ('w') - creates or overwrites the file ---
with open("output.txt", "w") as f:
    f.write("This is line 1.\n")
    f.write("This is line 2.\n")
    f.write("This is line 3.\n")

print("File 'output.txt' written successfully.")

print("\nContents after write:")
with open("output.txt", "r") as f:
    print(f.read())

# --- Append mode ('a') - adds to existing file ---
with open("output.txt", "a") as f:
    f.write("This line was appended.\n")
    f.write("Another appended line.\n")

print("Data appended successfully.")

print("\nContents after append:")
with open("output.txt", "r") as f:
    print(f.read())

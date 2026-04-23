# Q19. Program to copy contents of one file to another.

# Create source file
with open("source.txt", "w") as f:
    f.write("Line 1: Hello from source file!\n")
    f.write("Line 2: This will be copied.\n")
    f.write("Line 3: Python file handling.\n")

print("Source file 'source.txt' created.\n")

# Copy contents
source_file = "source.txt"
dest_file   = "destination.txt"

with open(source_file, "r") as src:
    content = src.read()

with open(dest_file, "w") as dest:
    dest.write(content)

print(f"Contents copied from '{source_file}' to '{dest_file}' successfully!")

# Verify
print("\nContents of source file:")
with open(source_file, "r") as f:
    print(f.read())

print("Contents of destination file:")
with open(dest_file, "r") as f:
    print(f.read())

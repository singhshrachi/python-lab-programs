# Q20. Program to demonstrate file pointer operations using seek().

# Create a file
with open("pointer.txt", "w") as f:
    f.write("Hello, Python File Handling!")

print("File 'pointer.txt' created.\n")

with open("pointer.txt", "r") as f:

    print(f"Initial position         : {f.tell()}")

    data = f.read(5)
    print(f"Read 5 chars             : '{data}'")
    print(f"Position after reading 5 : {f.tell()}")

    # seek(0) - go to beginning
    f.seek(0)
    print(f"\nAfter seek(0), position  : {f.tell()}")
    print(f"Read from beginning      : '{f.read(5)}'")

    # seek(7) - go to position 7
    f.seek(7)
    print(f"\nAfter seek(7), position  : {f.tell()}")
    print(f"Read from position 7     : '{f.read(6)}'")

    # seek(0, 2) - go to end of file
    f.seek(0, 2)
    print(f"\nEnd of file position     : {f.tell()}")

    # seek(0, 1) - current position (no change)
    f.seek(5)
    f.seek(3, 1)   # move 3 forward from current
    print(f"\nAfter seek(3,1) from 5   : position {f.tell()}")
    print(f"Read at that position    : '{f.read(5)}'")

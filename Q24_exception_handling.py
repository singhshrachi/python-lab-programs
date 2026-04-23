# Q24. Program to handle exceptions using try-except blocks.

# Example 1: ZeroDivisionError
print("Example 1: ZeroDivisionError")
try:
    result = 10 / 0
    print(f"Result: {result}")
except ZeroDivisionError as e:
    print(f"  Caught ZeroDivisionError: {e}")

# Example 2: ValueError
print("\nExample 2: ValueError")
try:
    num = int("abc")
except ValueError as e:
    print(f"  Caught ValueError: {e}")

# Example 3: TypeError
print("\nExample 3: TypeError")
try:
    result = "Hello" + 5
except TypeError as e:
    print(f"  Caught TypeError: {e}")

# Example 4: IndexError
print("\nExample 4: IndexError")
try:
    lst = [1, 2, 3]
    print(lst[10])
except IndexError as e:
    print(f"  Caught IndexError: {e}")

# Example 5: KeyError
print("\nExample 5: KeyError")
try:
    d = {"name": "Rahul"}
    print(d["age"])
except KeyError as e:
    print(f"  Caught KeyError: {e}")

# Example 6: FileNotFoundError
print("\nExample 6: FileNotFoundError")
try:
    with open("no_such_file.txt", "r") as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"  Caught FileNotFoundError: {e}")

# Example 7: User input with exception handling
print("\nExample 7: Safe user input")
try:
    age = int(input("Enter your age: "))
    print(f"  Your age is: {age}")
except ValueError as e:
    print(f"  Invalid input! Please enter a number. Error: {e}")

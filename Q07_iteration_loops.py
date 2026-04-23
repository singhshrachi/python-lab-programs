# Q7. Program to iterate through string, list, and dictionary using loops.

# Iterating through a String
my_string = "Python"
print("Iterating through String:")
for ch in my_string:
    print(f"  {ch}")

# Iterating through a List
my_list = [10, 20, 30, 40, 50]
print("\nIterating through List:")
for item in my_list:
    print(f"  {item}")

# Iterating through a Dictionary
my_dict = {"name": "Alice", "age": 21, "course": "BCA"}
print("\nIterating through Dictionary (keys):")
for key in my_dict:
    print(f"  {key}")

print("\nIterating through Dictionary (values):")
for value in my_dict.values():
    print(f"  {value}")

print("\nIterating through Dictionary (key-value pairs):")
for key, value in my_dict.items():
    print(f"  {key} : {value}")

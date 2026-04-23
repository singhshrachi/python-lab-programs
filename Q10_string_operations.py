# Q10. Program to perform string operations (slicing, concatenation, reversing).

s = "Hello, Python!"
print(f"Original string       : {s}")
print(f"Length                : {len(s)}")

# Slicing
print(f"\nSlicing [0:5]         : {s[0:5]}")
print(f"Slicing [7:]          : {s[7:]}")
print(f"Slicing [:5]          : {s[:5]}")
print(f"Every 2nd char [::2]  : {s[::2]}")

# Reversing
print(f"\nReversed [::-1]       : {s[::-1]}")

# Concatenation
s1 = "Hello"
s2 = " World"
print(f"\nConcatenation         : '{s1}' + '{s2}' = '{s1 + s2}'")

# Repetition
print(f"Repetition ('Hi' * 3) : {'Hi' * 3}")

# Other useful string methods
print(f"\nUppercase             : {s.upper()}")
print(f"Lowercase             : {s.lower()}")
print(f"Replace               : {s.replace('Python', 'World')}")
print(f"Find 'Python'         : index {s.find('Python')}")
print(f"Strip '  hello  '     : '{'  hello  '.strip()}'")
print(f"Split by space        : {s.split(' ')}")

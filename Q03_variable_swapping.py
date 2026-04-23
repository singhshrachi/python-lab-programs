# Q3. Program to demonstrate variable assignment and swapping values.

x = 100
y = 200
print(f"Before swap: x = {x}, y = {y}")

# Method 1: Using a temporary variable
temp = x
x = y
y = temp
print(f"\nAfter swap (using temp variable): x = {x}, y = {y}")

# Method 2: Pythonic one-liner swap
x, y = y, x
print(f"After swap (one-liner)          : x = {x}, y = {y}")

# Multiple assignment
a = b = c = 50
print(f"\nMultiple assignment (a = b = c = 50): a={a}, b={b}, c={c}")

# Simultaneous assignment
p, q, r = 1, 2, 3
print(f"Simultaneous assignment (p,q,r = 1,2,3): p={p}, q={q}, r={r}")

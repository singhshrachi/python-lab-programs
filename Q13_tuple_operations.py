# Q13. Program to perform tuple operations and demonstrate immutability.

t = (10, 20, 30, 40, 50)
print(f"Tuple           : {t}")
print(f"Length          : {len(t)}")
print(f"First element   : {t[0]}")
print(f"Last element    : {t[-1]}")
print(f"Slicing [1:4]   : {t[1:4]}")
print(f"Reversed        : {t[::-1]}")
print(f"Count of 20     : {t.count(20)}")
print(f"Index of 30     : {t.index(30)}")
print(f"Max             : {max(t)}")
print(f"Min             : {min(t)}")
print(f"Sum             : {sum(t)}")

# Concatenation
t2 = (60, 70)
print(f"\nConcatenated (t + t2): {t + t2}")

# Repetition
print(f"Repetition (t2 * 2) : {t2 * 2}")

# Tuple packing and unpacking
print(f"\nTuple Unpacking:")
a, b, c, d, e = t
print(f"  a={a}, b={b}, c={c}, d={d}, e={e}")

# Demonstrating Immutability
print(f"\nDemonstrating Immutability:")
try:
    t[0] = 999
except TypeError as e:
    print(f"  Error: {e}")
    print("  Tuples cannot be modified after creation!")

# Q15. Program using built-in functions on list, string, and dictionary.

# --- List ---
nums = [5, 3, 8, 1, 9, 2, 7]
print(f"List              : {nums}")
print(f"len()             : {len(nums)}")
print(f"max()             : {max(nums)}")
print(f"min()             : {min(nums)}")
print(f"sum()             : {sum(nums)}")
print(f"sorted()          : {sorted(nums)}")
print(f"sorted(desc)      : {sorted(nums, reverse=True)}")
print(f"list(range(1,6))  : {list(range(1, 6))}")
print(f"enumerate example:")
for i, val in enumerate(nums):
    print(f"  index {i} -> {val}")

# --- String ---
s = "hello world python"
print(f"\nString            : '{s}'")
print(f"len()             : {len(s)}")
print(f"upper()           : {s.upper()}")
print(f"title()           : {s.title()}")
print(f"capitalize()      : {s.capitalize()}")
print(f"split()           : {s.split()}")
print(f"count('l')        : {s.count('l')}")
print(f"strip()           : '{'  spaces  '.strip()}'")
print(f"replace()         : {s.replace('world', 'BCA')}")
print(f"startswith('hello'): {s.startswith('hello')}")
print(f"endswith('python') : {s.endswith('python')}")

# --- Dictionary ---
d = {"Math": 85, "Science": 90, "English": 78}
print(f"\nDictionary        : {d}")
print(f"len()             : {len(d)}")
print(f"max(values)       : {max(d.values())}")
print(f"min(values)       : {min(d.values())}")
print(f"sum(values)       : {sum(d.values())}")
print(f"sorted keys       : {sorted(d)}")
print(f"Subject with max marks: {max(d, key=d.get)}")

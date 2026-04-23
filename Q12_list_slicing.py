# Q12. Program to demonstrate list slicing and list manipulation.

lst = [10, 20, 30, 40, 50, 60, 70, 80]
print(f"Original list       : {lst}")

# Slicing
print(f"\nFirst 3 elements    : {lst[:3]}")
print(f"Last 3 elements     : {lst[-3:]}")
print(f"Middle [2:6]        : {lst[2:6]}")
print(f"Every 2nd element   : {lst[::2]}")
print(f"Reversed            : {lst[::-1]}")

# Manipulation
lst.append(90)
print(f"\nAfter append(90)    : {lst}")

lst.insert(2, 25)
print(f"After insert(2, 25) : {lst}")

lst.remove(25)
print(f"After remove(25)    : {lst}")

popped = lst.pop()
print(f"After pop()         : {lst}  (popped: {popped})")

lst.sort()
print(f"After sort()        : {lst}")

lst.reverse()
print(f"After reverse()     : {lst}")

print(f"\nLength  : {len(lst)}")
print(f"Max     : {max(lst)}")
print(f"Min     : {min(lst)}")
print(f"Sum     : {sum(lst)}")
print(f"Index of 50 : {lst.index(50)}")
print(f"Count of 10 : {lst.count(10)}")

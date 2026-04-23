# Q9. Demonstrate use of break, continue, and pass in loops.

# --- break ---
print("break example (stop loop when i == 5):")
for i in range(1, 11):
    if i == 5:
        print(f"  Breaking at {i}!")
        break
    print(f"  i = {i}")

# --- continue ---
print("\ncontinue example (skip even numbers):")
for i in range(1, 11):
    if i % 2 == 0:
        continue      # skip even numbers
    print(f"  i = {i}")

# --- pass ---
print("\npass example (placeholder, does nothing for even numbers):")
for i in range(1, 6):
    if i % 2 == 0:
        pass          # do nothing, just a placeholder
    else:
        print(f"  Odd number: {i}")

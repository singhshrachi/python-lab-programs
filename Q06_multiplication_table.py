# Q6. Program using for loop to print multiplication table of a number.

n = int(input("Enter a number: "))

print(f"\nMultiplication Table of {n}:")
print("-" * 20)
for i in range(1, 11):
    print(f"{n} x {i:2} = {n * i}")

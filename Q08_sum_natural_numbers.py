# Q8. Program using while loop to compute sum of first N natural numbers.

N = int(input("Enter N: "))

total = 0
i = 1

while i <= N:
    total += i
    i += 1

print(f"\nSum of first {N} natural numbers = {total}")
print(f"Formula verification: N*(N+1)/2 = {N*(N+1)//2}")

# Q4. Program using if-else to find the largest of three numbers.

a = float(input("Enter first number : "))
b = float(input("Enter second number: "))
c = float(input("Enter third number : "))

if a >= b and a >= c:
    print(f"\nLargest number is: {a}")
elif b >= a and b >= c:
    print(f"\nLargest number is: {b}")
else:
    print(f"\nLargest number is: {c}")

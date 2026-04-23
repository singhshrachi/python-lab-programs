# Q2. Program to perform all arithmetic operations on user input numbers.

num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number: "))

print(f"\nAddition       : {num1} + {num2} = {num1 + num2}")
print(f"Subtraction    : {num1} - {num2} = {num1 - num2}")
print(f"Multiplication : {num1} * {num2} = {num1 * num2}")

if num2 != 0:
    print(f"Division       : {num1} / {num2} = {num1 / num2}")
    print(f"Floor Division : {num1} // {num2} = {num1 // num2}")
    print(f"Modulus        : {num1} % {num2} = {num1 % num2}")
else:
    print("Division / Floor Division / Modulus: Cannot divide by zero!")

print(f"Exponentiation : {num1} ** {num2} = {num1 ** num2}")

# Q5. Program using nested if to classify a number (positive, negative, zero).

num = float(input("Enter a number: "))

if num != 0:
    if num > 0:
        print(f"{num} is a Positive number.")
    else:
        print(f"{num} is a Negative number.")
else:
    print("The number is Zero.")

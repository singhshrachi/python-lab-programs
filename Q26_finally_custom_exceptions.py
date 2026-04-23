# Q26. Program using finally and custom exceptions.

# --- finally block ---
print("=== finally Block ===")

def read_file_safe(filename):
    f = None
    try:
        f = open(filename, "r")
        content = f.read()
        print(f"  File read: {len(content)} characters.")
        return content
    except FileNotFoundError:
        print(f"  File '{filename}' not found!")
    finally:
        if f:
            f.close()
        print("  finally: cleanup done.\n")

# Create a test file
with open("test.txt", "w") as f:
    f.write("Hello from test file!")

read_file_safe("test.txt")
read_file_safe("nonexistent.txt")


# --- Custom Exceptions ---
print("=== Custom Exceptions ===\n")

class AgeError(Exception):
    """Raised when age is out of valid range."""
    def __init__(self, age, message="Age must be between 1 and 120"):
        self.age     = age
        self.message = message
        super().__init__(self.message)

class NegativeNumberError(Exception):
    """Raised when a negative number is not allowed."""
    pass

class InsufficientBalanceError(Exception):
    """Raised when bank balance is insufficient."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount  = amount
        super().__init__(f"Cannot withdraw {amount}. Balance is only {balance}.")


# Test AgeError
def validate_age(age):
    if age < 1 or age > 120:
        raise AgeError(age)
    return f"Valid age: {age}"

print("--- AgeError ---")
for age in [25, -5, 200]:
    try:
        print(f"  {validate_age(age)}")
    except AgeError as e:
        print(f"  AgeError (age={e.age}): {e.message}")


# Test NegativeNumberError
def square_root(n):
    if n < 0:
        raise NegativeNumberError(f"Cannot compute square root of {n}!")
    return n ** 0.5

print("\n--- NegativeNumberError ---")
for n in [16, -4, 25]:
    try:
        print(f"  sqrt({n}) = {square_root(n)}")
    except NegativeNumberError as e:
        print(f"  Error: {e}")


# Test InsufficientBalanceError
def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError(balance, amount)
    return balance - amount

print("\n--- InsufficientBalanceError ---")
try:
    new_balance = withdraw(5000, 3000)
    print(f"  Withdrawal successful! New balance: {new_balance}")
    new_balance = withdraw(new_balance, 5000)
except InsufficientBalanceError as e:
    print(f"  Error: {e}")

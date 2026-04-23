# Q25. Program demonstrating multiple exceptions handling.

# Method 1: Multiple except blocks
def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"
    except TypeError:
        return "Error: Invalid data types for division!"
    except Exception as e:
        return f"Unexpected Error: {e}"

print("=== Method 1: Separate except blocks ===")
print(f"10 / 2     : {safe_divide(10, 2)}")
print(f"10 / 0     : {safe_divide(10, 0)}")
print(f"'a' / 2    : {safe_divide('a', 2)}")

# Method 2: Multiple exceptions in one except block
print("\n=== Method 2: Multiple exceptions in one line ===")
test_values = ["42", "abc", None, "3.14", 0]
for val in test_values:
    try:
        result = int(val)
        print(f"  int({val!r}) = {result}")
    except (ValueError, TypeError) as e:
        print(f"  int({val!r}) -> Error: {e}")

# Method 3: Catching all exceptions with base Exception
print("\n=== Method 3: Chained multiple handlers ===")
def risky_operation(data, index, divisor):
    try:
        result = data[index] / divisor
        print(f"  Result: {result}")
    except IndexError:
        print("  IndexError: List index out of range!")
    except ZeroDivisionError:
        print("  ZeroDivisionError: Cannot divide by zero!")
    except TypeError:
        print("  TypeError: Invalid operation on given types!")
    except Exception as e:
        print(f"  Unexpected Error: {type(e).__name__}: {e}")

data = [10, 20, 30]
risky_operation(data, 1, 4)    # Success
risky_operation(data, 10, 4)   # IndexError
risky_operation(data, 1, 0)    # ZeroDivisionError
risky_operation(data, 1, "x")  # TypeError

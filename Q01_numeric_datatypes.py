# Q1. Program to demonstrate different numeric data types (int, float) and type conversion.

# Integer
a = 10
print(f"Integer value : {a}, Type: {type(a)}")

# Float
b = 3.14
print(f"Float value   : {b}, Type: {type(b)}")

# Type Conversions
a_to_float = float(a)
print(f"\nint to float  : {a_to_float}, Type: {type(a_to_float)}")

b_to_int = int(b)
print(f"float to int  : {b_to_int},  Type: {type(b_to_int)}")

s1 = "42"
s2 = "3.99"
print(f"\nstr '42' to int   : {int(s1)},  Type: {type(int(s1))}")
print(f"str '3.99' to float: {float(s2)}, Type: {type(float(s2))}")

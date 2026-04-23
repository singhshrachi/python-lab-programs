# Q14. Program to perform dictionary operations (add, update, delete).

student = {
    "name"  : "Rahul",
    "age"   : 20,
    "course": "BCA"
}
print(f"Original dictionary  : {student}")

# Add
student["city"] = "Sagar"
print(f"\nAfter adding 'city'  : {student}")

# Update
student["age"] = 21
print(f"After updating age   : {student}")

# Delete using del
del student["city"]
print(f"After del 'city'     : {student}")

# Delete using pop()
removed = student.pop("age")
print(f"After pop('age')     : {student}  (removed: {removed})")

# Other methods
student["age"] = 21
student["city"] = "Bhopal"
print(f"\nDictionary now       : {student}")
print(f"Keys                 : {list(student.keys())}")
print(f"Values               : {list(student.values())}")
print(f"Items                : {list(student.items())}")
print(f"get('name')          : {student.get('name')}")
print(f"get('phone', 'N/A')  : {student.get('phone', 'N/A')}")
print(f"'name' in dict?      : {'name' in student}")

# clear()
student2 = {"a": 1, "b": 2}
student2.clear()
print(f"\nAfter clear()        : {student2}")

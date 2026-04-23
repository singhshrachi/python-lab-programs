# Q27. Program using numpy to perform array operations (creation, indexing, arithmetic).

import numpy as np

# --- Creation ---
print("=== Array Creation ===")
a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])
print(f"Array a         : {a}")
print(f"Array b         : {b}")
print(f"Shape of a      : {a.shape}")
print(f"Dtype of a      : {a.dtype}")
print(f"ndim of a       : {a.ndim}")

print(f"\nnp.zeros((2,3)) :\n{np.zeros((2, 3))}")
print(f"np.ones((2,3))  :\n{np.ones((2, 3))}")
print(f"np.arange(0,10,2): {np.arange(0, 10, 2)}")
print(f"np.linspace(0,1,5): {np.linspace(0, 1, 5)}")

# 2D array
print("\n=== 2D Array ===")
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print(f"Matrix:\n{matrix}")
print(f"Shape: {matrix.shape}")

# --- Indexing ---
print("\n=== Indexing ===")
print(f"a[0]             : {a[0]}")
print(f"a[-1]            : {a[-1]}")
print(f"a[1:4]           : {a[1:4]}")
print(f"a[::2]           : {a[::2]}")
print(f"matrix[1][2]     : {matrix[1][2]}")
print(f"matrix[:, 1]     : {matrix[:, 1]}")   # All rows, column 1
print(f"matrix[0, :]     : {matrix[0, :]}")   # Row 0

# --- Arithmetic ---
print("\n=== Arithmetic Operations ===")
print(f"a + b            : {a + b}")
print(f"a - b            : {a - b}")
print(f"a * b            : {a * b}")
print(f"b / a            : {b / a}")
print(f"a ** 2           : {a ** 2}")
print(f"a + 100          : {a + 100}")

# --- Universal Functions ---
print("\n=== Universal Functions ===")
print(f"np.sqrt(a)       : {np.sqrt(a)}")
print(f"np.sum(a)        : {np.sum(a)}")
print(f"np.mean(a)       : {np.mean(a)}")
print(f"np.max(b)        : {np.max(b)}")
print(f"np.min(b)        : {np.min(b)}")
print(f"np.std(a)        : {np.std(a):.4f}")

# Matrix operations
print("\n=== Matrix Operations ===")
print(f"Matrix transpose:\n{matrix.T}")
print(f"Matrix * 2:\n{matrix * 2}")

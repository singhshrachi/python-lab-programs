# Q31. Program combining numpy, pandas, and matplotlib for simple data analysis.

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")  # Non-interactive backend (remove this line in lab if using IDE)
import matplotlib.pyplot as plt

# --- Step 1: Create Dataset using NumPy ---
np.random.seed(42)
n = 50

data = {
    "Student_ID": range(1, n + 1),
    "Math"      : np.random.randint(50, 100, n),
    "Science"   : np.random.randint(45, 100, n),
    "English"   : np.random.randint(55, 100, n),
    "Computer"  : np.random.randint(60, 100, n),
}

# --- Step 2: Analyse with Pandas ---
df = pd.DataFrame(data)
df["Total"]   = df[["Math", "Science", "English", "Computer"]].sum(axis=1)
df["Average"] = (df["Total"] / 4).round(2)
df["Grade"]   = pd.cut(
    df["Average"],
    bins=[0, 60, 70, 80, 90, 100],
    labels=["F", "C", "B", "A", "A+"]
)

print("=== First 10 rows of Dataset ===")
print(df.head(10).to_string(index=False))

print("\n=== Statistical Summary ===")
print(df[["Math", "Science", "English", "Computer", "Average"]].describe().round(2))

# NumPy computations
avg_array = df["Average"].values
print(f"\n=== NumPy Computations ===")
print(f"Mean Average   : {np.mean(avg_array):.2f}")
print(f"Std Deviation  : {np.std(avg_array):.2f}")
print(f"Median         : {np.median(avg_array):.2f}")
print(f"Variance       : {np.var(avg_array):.2f}")

print("\n=== Grade Distribution ===")
print(df["Grade"].value_counts().sort_index())

print("\n=== Top 5 Students ===")
top5 = df.nlargest(5, "Average")[["Student_ID", "Math", "Science", "English", "Computer", "Average", "Grade"]]
print(top5.to_string(index=False))

# --- Step 3: Visualize with Matplotlib ---
fig, axes = plt.subplots(2, 2, figsize=(13, 9))
fig.suptitle("Student Performance Analysis\n(NumPy + Pandas + Matplotlib)", fontsize=14)

# Plot 1: Average marks per subject (bar chart)
subjects = ["Math", "Science", "English", "Computer"]
averages = [df[s].mean() for s in subjects]
bars = axes[0, 0].bar(subjects, averages, color=["#4e79a7", "#f28e2b", "#59a14f", "#e15759"], edgecolor="black")
axes[0, 0].set_title("Average Marks by Subject")
axes[0, 0].set_ylabel("Average Marks")
axes[0, 0].set_ylim(0, 100)
for bar, val in zip(bars, averages):
    axes[0, 0].text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1,
                    f"{val:.1f}", ha="center", fontsize=9)

# Plot 2: Grade distribution (pie chart)
grade_counts = df["Grade"].value_counts().sort_index()
axes[0, 1].pie(grade_counts, labels=grade_counts.index,
               autopct="%1.1f%%", startangle=90,
               colors=["#d62728", "#ff7f0e", "#2ca02c", "#1f77b4", "#9467bd"])
axes[0, 1].set_title("Grade Distribution")

# Plot 3: Line plot - Average marks of first 20 students
axes[1, 0].plot(df["Student_ID"][:20], df["Average"][:20],
                marker="o", color="purple", linewidth=1.5, markersize=5)
mean_val = df["Average"].mean()
axes[1, 0].axhline(y=mean_val, color="red", linestyle="--",
                   label=f"Overall Mean: {mean_val:.1f}")
axes[1, 0].set_title("Average Marks - First 20 Students")
axes[1, 0].set_xlabel("Student ID")
axes[1, 0].set_ylabel("Average Marks")
axes[1, 0].legend()
axes[1, 0].grid(True, alpha=0.4)

# Plot 4: Histogram of averages
axes[1, 1].hist(df["Average"], bins=10, color="steelblue", edgecolor="black", alpha=0.8)
axes[1, 1].set_title("Distribution of Average Marks")
axes[1, 1].set_xlabel("Average Marks")
axes[1, 1].set_ylabel("Number of Students")
axes[1, 1].grid(True, alpha=0.4)

plt.tight_layout()
plt.savefig("Q31_analysis.png", dpi=100)
plt.close()

print("\nAnalysis chart saved as 'Q31_analysis.png'")
print("Open the file to view the graphs.")

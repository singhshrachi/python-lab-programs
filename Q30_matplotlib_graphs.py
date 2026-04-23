# Q30. Program using matplotlib to plot line and bar graphs.

import matplotlib
matplotlib.use("Agg")  # Non-interactive backend (remove this line in lab if using IDE)
import matplotlib.pyplot as plt

# --- Line Graph ---
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales  = [150, 200, 175, 220, 250, 210]

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(months, sales, marker="o", color="blue", linewidth=2, markersize=8, linestyle="-")
plt.title("Monthly Sales - Line Graph", fontsize=13)
plt.xlabel("Month")
plt.ylabel("Sales (units)")
plt.grid(True, linestyle="--", alpha=0.6)
for i, val in enumerate(sales):
    plt.text(i, val + 3, str(val), ha="center", fontsize=9)

# --- Bar Graph ---
courses  = ["BCA", "MCA", "BSc", "BBA"]
students = [120, 80, 100, 90]
colors   = ["steelblue", "orange", "green", "tomato"]

plt.subplot(1, 2, 2)
bars = plt.bar(courses, students, color=colors, edgecolor="black", width=0.5)
plt.title("Student Enrollment - Bar Graph", fontsize=13)
plt.xlabel("Course")
plt.ylabel("Number of Students")
plt.ylim(0, 140)
for bar, val in zip(bars, students):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 2,
             str(val), ha="center", fontsize=10)

plt.tight_layout()
plt.savefig("Q30_graphs.png", dpi=100)
plt.close()

print("Line and Bar graphs saved as 'Q30_graphs.png'")
print("Open the file to view the graphs.")

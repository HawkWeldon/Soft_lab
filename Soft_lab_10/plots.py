
import numpy as np
import matplotlib.pyplot as plt

# Create a directory for the plots

np.random.seed(42)

# 1. Line Plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, color="blue", linestyle="--", label="sin(x)")
plt.title("Sine Function")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.legend()
plt.grid(True)
plt.savefig("line_plot.pdf", bbox_inches="tight")
plt.close()

# 2. Bar Chart
categories = ["A", "B", "C", "D", "E"]
values = [15, 25, 10, 30, 20]

plt.figure(figsize=(8, 5))
plt.bar(categories, values, color="orange")
plt.title("Category Comparison")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.savefig("bar_chart.pdf", bbox_inches="tight")
plt.close()

# 3. Histogram
data = np.random.normal(loc=50, scale=10, size=1000)

plt.figure(figsize=(8, 5))
plt.hist(data, bins=30, color="green", edgecolor="black")
plt.title("Normal Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.savefig("histogram.pdf", bbox_inches="tight")
plt.close()

# 4. Scatter Plot
x = np.random.rand(100)
y = 2 * x + np.random.normal(0, 0.2, 100)

plt.figure(figsize=(8, 5))
plt.scatter(x, y, color="purple", alpha=0.6)
plt.title("Scatter Plot with Noise")
plt.xlabel("X")
plt.ylabel("Y")
plt.savefig("scatter_plot.pdf", bbox_inches="tight")
plt.close()

print("All four plots saved successfully!")

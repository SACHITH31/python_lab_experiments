# 28
import pandas as pd

data = {
    "A": list(range(1, 11)),
    "B": list(range(11, 21)),
    "C": list(range(21, 31)),
    "D": list(range(31, 41)),
    "E": list(range(41, 51))
}

df = pd.DataFrame(data)

# a) Head
print(df.head())

# b) Data selection
print("Column A:\n", df["A"])
print("Multiple columns:\n", df[["A", "B"]])
print("Row selection:\n", df.iloc[0:3])


# 29
# scatter means dots, plot means line
import matplotlib.pyplot as plt

# Selecting two columns
x = df["A"]
y = df["B"]

# Scatter plot
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("A")
plt.ylabel("B")
plt.show()

# Line plot
plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("A")
plt.ylabel("B")
plt.show()

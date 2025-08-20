# notebook.py
# Email: 22f3002631@ds.study.iitm.ac.in
# Marimo Interactive Notebook Example
# Demonstrates variable dependencies, interactive widgets, and dynamic markdown

import marimo as mo

# -----------------------------
# Cell 1: Import dataset (synthetic for demo)
# -----------------------------
# This cell creates a simple dataset of x values and their squares.
# Later cells will depend on this dataset.
x_values = list(range(1, 51))  # numbers from 1 to 50
y_values = [x**2 for x in x_values]  # squared values


# -----------------------------
# Cell 2: Interactive widget
# -----------------------------
# Create an interactive slider to pick how many data points to visualize.
slider = mo.ui.slider(start=5, stop=50, step=5, value=10)


# -----------------------------
# Cell 3: Data subset depending on slider
# -----------------------------
# This cell dynamically subsets the dataset based on slider.value
subset_x = x_values[:slider.value]
subset_y = y_values[:slider.value]


# -----------------------------
# Cell 4: Dynamic Markdown output
# -----------------------------
# Show the number of selected points and simple visualization with emojis.
mo.md(
    f"""
    ### 📊 Data Subset Preview  
    You selected **{slider.value}** points.  
    First few x values: {subset_x[:5]}  
    First few y values: {subset_y[:5]}  

    Progress: {"🟢" * (slider.value // 5)}
    """
)


# -----------------------------
# Cell 5: Plotting (optional visualization)
# -----------------------------
# Create a simple scatter plot of the subset.
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.scatter(subset_x, subset_y, c="blue")
ax.set_xlabel("x")
ax.set_ylabel("y = x²")
ax.set_title(f"Scatter plot of first {slider.value} points")
fig

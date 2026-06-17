# Task 1: Plotting with Pandas (Employee Revenue Bar Chart)
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# 1. Connect to the database
# Note: The 'db' folder must be in the parent directory of your 'assignment11' folder
db_path = "../db/lesson.db"
conn = sqlite3.connect(db_path)

# 2. The exact SQL query provided in the assignment instructions
sql_query = """
SELECT last_name, SUM(price*quantity) AS revenue
FROM employees e
JOIN orders o ON e.employee_id = o.employee_id
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY e.employee_id;
"""

# 3. Load the data into a Pandas DataFrame
employee_results = pd.read_sql_query(sql_query, conn)
conn.close()

print("Data loaded successfully:")
print(employee_results, "\n")

# 4. Set the index to 'last_name' so it appears on the x-axis
employee_results.set_index('last_name', inplace=True)

# 5. Create a bar chart using Pandas plotting functionality
ax = employee_results['revenue'].plot(
    kind='bar', 
    color='skyblue', 
    edgecolor='black',
    figsize=(10, 6)
)

# 6. Add appropriate titles, labels, and formatting
plt.title("Total Revenue by Employee", fontsize=14, fontweight='bold')
plt.xlabel("Employee Last Name", fontsize=12)
plt.ylabel("Revenue ($)", fontsize=12)
plt.xticks(rotation=45, ha='right')  # Rotate labels so they don't overlap
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout to prevent labels from getting cut off
plt.tight_layout()

# 7. Show the plot
plt.show()

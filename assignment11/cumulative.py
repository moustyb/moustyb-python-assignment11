# Task 2: A Line Plot with Pandas (Cumulative Revenue)
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# 1. Connect to the database
db_path = "../db/lesson.db"
conn = sqlite3.connect(db_path)

# 2. SQL query to get order_id and total_price for each order
sql_query = """
SELECT o.order_id, SUM(p.price * l.quantity) AS total_price
FROM orders o
JOIN line_items l ON o.order_id = l.order_id
JOIN products p ON l.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id;
"""

# 3. Load the data into a Pandas DataFrame
df = pd.read_sql_query(sql_query, conn)
conn.close()

print("Data loaded successfully:")
print(df.head(), "\n")

# 4. Add a "cumulative" column using cumsum()
df['cumulative'] = df['total_price'].cumsum()

# 5. Create a line plot of cumulative revenue vs. order_id
plt.figure(figsize=(10, 6))
plt.plot(df['order_id'], df['cumulative'], marker='o', linestyle='-', color='purple', linewidth=2)

# 6. Add appropriate titles, labels, and formatting
plt.title("Cumulative Revenue Over Time (by Order ID)", fontsize=14, fontweight='bold')
plt.xlabel("Order ID", fontsize=12)
plt.ylabel("Cumulative Revenue ($)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)

# Adjust layout to prevent labels from getting cut off
plt.tight_layout()

# 7. Show the plot
plt.show()

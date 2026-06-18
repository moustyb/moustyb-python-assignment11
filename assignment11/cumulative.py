# Task 2: A Line Plot with Pandas (Cumulative Revenue)
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

print("🚀 Starting Task 2: Cumulative Revenue Plot...")

# 1. Connect to the database
db_path = "../db/lesson.db"
try:
    conn = sqlite3.connect(db_path)
    print("✅ Successfully connected to database")
except Exception as e:
    print(f"❌ FAILED to connect: {e}")
    exit()

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
try:
    df = pd.read_sql_query(sql_query, conn)
    conn.close()
    print(f"✅ Successfully loaded {len(df)} orders")
except Exception as e:
    print(f"❌ FAILED to load data: {e}")
    exit()

# 4. Add a "cumulative" column using cumsum()
df['cumulative'] = df['total_price'].cumsum()
print("✅ Successfully calculated cumulative revenue")

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

# 7. IMPORTANT: Save the plot BEFORE showing it!
plt.savefig('cumulative_chart.png')
print("✅ Successfully saved chart to 'cumulative_chart.png'")

# 8. Show the plot
plt.show()
print("✅ Task 2 completed successfully!")
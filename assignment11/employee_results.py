import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect('../db/lesson.db')

# SQL query to get employee revenue
query = """
SELECT last_name, SUM(price*quantity) AS revenue 
FROM employees e 
JOIN orders o ON e.employee_id = o.employee_id 
JOIN line_items l ON o.order_id = l.order_id 
JOIN products p ON l.product_id = p.product_id 
GROUP BY e.employee_id;
"""

# Load data into a Pandas DataFrame
df = pd.read_sql_query(query, conn)
conn.close()

# Create a bar chart
df.plot(x='last_name', y='revenue', kind='bar', color='skyblue', title='Employee Revenue')

# Add labels
plt.xlabel('Employee Last Name')
plt.ylabel('Revenue ($)')
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()

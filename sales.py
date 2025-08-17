# Task 7 DA - Basic Sales Summary using SQLite and Python
# Save this file as task7_sales_summary.py and run it in Python IDLE

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Connect to SQLite database (will create if it doesn't exist)
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Step 2: Create sales table (if not exists)
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

# Step 3: Insert sample data (only if table is empty)
cursor.execute("SELECT COUNT(*) FROM sales")
if cursor.fetchone()[0] == 0:
    sample_data = [
        ("Laptop", 5, 800),
        ("Phone", 10, 500),
        ("Tablet", 7, 300),
        ("Headphones", 15, 50),
        ("Monitor", 6, 200),
        ("Keyboard", 12, 40),
        ("Mouse", 20, 25)
    ]
    cursor.executemany("INSERT INTO sales VALUES (?, ?, ?)", sample_data)
    conn.commit()

# Step 4: Run SQL query
query = """
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product;
"""

df = pd.read_sql_query(query, conn)

# Step 5: Print results
print("📊 Sales Summary by Product")
print(df)

# Step 6: Plot simple bar chart (Revenue by Product)
plt.figure(figsize=(8, 5))
plt.bar(df["product"], df["revenue"])
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.title("Revenue by Product")
plt.xticks(rotation=45)
plt.show()

# Step 7: Close connection
conn.close()

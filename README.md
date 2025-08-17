# SQL-using-Python
 Task 7 - Basic Sales Summary using SQLite and Python

 📌 Objective
The goal of this task was to create a **tiny SQLite database** and generate a **basic sales summary** using Python.  
We calculated total quantity sold and revenue per product, then displayed the results in both **tabular form** and a **bar chart**.

---

## ⚙️ Tools Used
- Python 3.13  
- SQLite (built into Python, no setup required)  
- Pandas (for handling SQL query results)  
- Matplotlib (for visualization)  



## 🗂 Dataset
We created a small SQLite database sales_data.db with one table:  

sales
- product (TEXT)  
- quantity (INTEGER)  
- price (REAL)  

Sample data was inserted into the table (e.g., Laptop, Phone, Tablet, etc.).

---

## 📝 Steps Performed
1. Connected Python to SQLite database (sqlite3.connect("sales_data.db")).
2. Created the sales table (if not exists).
3. Inserted sample sales data (only if table was empty).
4. Wrote and executed an SQL query:
   sql
   SELECT 
       product,
       SUM(quantity) AS total_qty,
       SUM(quantity * price) AS revenue
   FROM sales
   GROUP BY product;

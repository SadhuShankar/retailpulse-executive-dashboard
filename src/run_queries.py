import sqlite3
import pandas as pd

# Connect Database
conn = sqlite3.connect("data/ecommerce.db")

# SQL Query
query = """
SELECT
    payment_type,
    ROUND(SUM(payment_value),2) AS Revenue,

    ROW_NUMBER() OVER(
        ORDER BY SUM(payment_value) DESC
    ) AS Row_Number

FROM payments

GROUP BY payment_type;
"""

# Execute Query
result = pd.read_sql_query(query, conn)

print("=" * 40)
print("TOTAL ORDERS")
print("=" * 40)

print(result)

conn.close()
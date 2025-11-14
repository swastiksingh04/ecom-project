import sqlite3
import pandas as pd

conn = sqlite3.connect('ecom.db')
query = """
SELECT 
    c.name AS customer_name,
    p.name AS product_name,
    o.quantity,
    (o.quantity * p.price) AS total_price,
    o.order_date
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN products p ON o.product_id = p.product_id
ORDER BY o.order_date DESC;
"""

df = pd.read_sql_query(query, conn)
df.to_csv('query_output.csv', index=False)

conn.close()
print("Query output saved to query_output.csv")

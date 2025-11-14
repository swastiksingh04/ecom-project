import sqlite3
import pandas as pd

# Connect to SQLite database (creates ecom.db if it doesn't exist)
conn = sqlite3.connect('ecom.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    location TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT,
    price REAL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    order_date TEXT,
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY(product_id) REFERENCES products(product_id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS reviews (
    review_id INTEGER PRIMARY KEY,
    product_id INTEGER,
    customer_id INTEGER,
    rating INTEGER,
    comment TEXT,
    FOREIGN KEY(product_id) REFERENCES products(product_id),
    FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS inventory (
    product_id INTEGER PRIMARY KEY,
    stock_level INTEGER,
    restock_date TEXT,
    FOREIGN KEY(product_id) REFERENCES products(product_id)
)
''')

# Load CSVs into tables
def load_csv_to_sqlite(csv_file, table_name):
    df = pd.read_csv(csv_file)
    df.to_sql(table_name, conn, if_exists='replace', index=False)

load_csv_to_sqlite('customers.csv', 'customers')
load_csv_to_sqlite('products.csv', 'products')
load_csv_to_sqlite('orders.csv', 'orders')
load_csv_to_sqlite('reviews.csv', 'reviews')
load_csv_to_sqlite('inventory.csv', 'inventory')

conn.commit()
conn.close()

print("Data successfully ingested into SQLite database.")

import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# 1. Customers
customers = pd.DataFrame([{
    'customer_id': i,
    'name': fake.name(),
    'email': fake.email(),
    'location': fake.city()
} for i in range(1, 21)])
customers.to_csv('customers.csv', index=False)

# 2. Products
products = pd.DataFrame([{
    'product_id': i,
    'name': fake.word().capitalize(),
    'category': random.choice(['Electronics', 'Clothing', 'Books', 'Home']),
    'price': round(random.uniform(10, 500), 2)
} for i in range(1, 11)])
products.to_csv('products.csv', index=False)

# 3. Orders
orders = pd.DataFrame([{
    'order_id': i,
    'customer_id': random.randint(1, 20),
    'product_id': random.randint(1, 10),
    'quantity': random.randint(1, 5),
    'order_date': (datetime.now() - timedelta(days=random.randint(1, 365))).strftime('%Y-%m-%d')
} for i in range(1, 31)])
orders.to_csv('orders.csv', index=False)

# 4. Reviews
reviews = pd.DataFrame([{
    'review_id': i,
    'product_id': random.randint(1, 10),
    'customer_id': random.randint(1, 20),
    'rating': random.randint(1, 5),
    'comment': fake.sentence()
} for i in range(1, 21)])
reviews.to_csv('reviews.csv', index=False)

# 5. Inventory
inventory = pd.DataFrame([{
    'product_id': i,
    'stock_level': random.randint(0, 100),
    'restock_date': (datetime.now() + timedelta(days=random.randint(1, 30))).strftime('%Y-%m-%d')
} for i in range(1, 11)])
inventory.to_csv('inventory.csv', index=False)

print("Synthetic data files created successfully.")

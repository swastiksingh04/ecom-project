🛒 E-Commerce Synthetic Data Project

This project demonstrates an end-to-end workflow for synthetic e-commerce data generation, storage, querying, and analysis using Python and SQLite. It is ideal for data engineering + data analysis practice.

📂 Project Structure
├── synthetic_data.py       # Generates fake e-commerce CSV datasets
├── ingest_to_sqlite.py     # Loads generated CSVs into SQLite database (ecom.db)
├── query_sqlite.py         # Runs SQL joins and exports result to query_output.csv
├── customers.csv
├── products.csv
├── orders.csv
├── reviews.csv
├── inventory.csv
├── query_output.csv         # Final query result
└── README.md                # Documentation

🚀 How to Use
1. Clone the Repository
git clone https://github.com/swastiksingh04/ecom-project.git
cd ecom-project

2. Install Dependencies

Make sure Python 3.x is installed. Then install required libraries:

pip install faker pandas

3. Generate Synthetic Data
python synthetic_data.py


This will create the following CSV files:

customers.csv

products.csv

orders.csv

reviews.csv

inventory.csv

4. Ingest Data into SQLite
python ingest_to_sqlite.py


This creates ecom.db and loads all CSVs into corresponding tables.

5. Run SQL Query
python query_sqlite.py


This generates query_output.csv containing joined customer, product, and order information.

📊 Example Output (query_output.csv)
customer_name	product_name	quantity	total_price	order_date
John Doe	Laptop	2	1200.00	2025-03-14
Jane Smith	T-Shirt	1	25.00	2025-02-10
🛠️ Requirements

Python 3.x

Libraries:

faker

pandas

SQLite (comes bundled with Python)

🎯 Purpose

This project is designed to:

Generate realistic synthetic e-commerce datasets

Demonstrate database ingestion using SQLite

Perform SQL joins and analysis

Provide a complete reproducible workflow for learning data engineering + analytics

📌 Author

Created by: Swastik Singh
GitHub: @swastiksingh04

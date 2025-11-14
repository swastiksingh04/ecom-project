# 🛒 E-Commerce Synthetic Data Project

This project demonstrates an end-to-end workflow for **synthetic e-commerce data generation, storage, and analysis** using Python and SQLite.

---

## 📂 Project Structure

- `synthetic_data.py` → Generates fake customers, products, orders, reviews, and inventory data into CSV files.
- `ingest_to_sqlite.py` → Loads the generated CSV files into an SQLite database (`ecom.db`).
- `query_sqlite.py` → Runs SQL queries to join tables and outputs results into `query_output.csv`.
- `customers.csv`, `products.csv`, `orders.csv`, `reviews.csv`, `inventory.csv` → Synthetic data files.
- `query_output.csv` → Final query result (customers + products + orders).
- `README.md` → Documentation.

---

## 🚀 How to Use

### 1. Clone the Repository
```bash
git clone https://github.com/swastiksingh04/ecom-project.git
cd ecom-project

# E-Commerce Synthetic Data Project

This project demonstrates an end-to-end workflow for synthetic e-commerce data generation using Python and SQLite.

Project Structure:
- synthetic_data.py: Generates fake CSVs
- ingest_to_sqlite.py: Loads CSVs into SQLite
- query_sqlite.py: Runs joins and exports output
- customers.csv, products.csv, orders.csv, reviews.csv, inventory.csv
- query_output.csv

Usage:
1. Clone repo
2. Install deps: pip install faker pandas
3. Run synthetic_data.py
4. Run ingest_to_sqlite.py
5. Run query_sqlite.py

Author: Swastik Singh

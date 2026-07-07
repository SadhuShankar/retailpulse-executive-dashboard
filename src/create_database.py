import sqlite3
import pandas as pd

# Create Database
conn = sqlite3.connect("data/ecommerce.db")

print("✅ Database Created")

# -------------------------------
# Load CSV Files
# -------------------------------

customers = pd.read_csv("data/olist_customers_dataset.csv")
orders = pd.read_csv("data/olist_orders_dataset.csv")
order_items = pd.read_csv("data/olist_order_items_dataset.csv")
payments = pd.read_csv("data/olist_order_payments_dataset.csv")
products = pd.read_csv("data/olist_products_dataset.csv")
sellers = pd.read_csv("data/olist_sellers_dataset.csv")
reviews = pd.read_csv("data/olist_order_reviews_dataset.csv")
translation = pd.read_csv("data/product_category_name_translation.csv")

# -------------------------------
# Store in SQLite
# -------------------------------

customers.to_sql("customers", conn, if_exists="replace", index=False)
orders.to_sql("orders", conn, if_exists="replace", index=False)
order_items.to_sql("order_items", conn, if_exists="replace", index=False)
payments.to_sql("payments", conn, if_exists="replace", index=False)
products.to_sql("products", conn, if_exists="replace", index=False)
sellers.to_sql("sellers", conn, if_exists="replace", index=False)
reviews.to_sql("reviews", conn, if_exists="replace", index=False)
translation.to_sql("translation", conn, if_exists="replace", index=False)

conn.close()

print("✅ All Tables Imported Successfully!")
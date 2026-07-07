import pandas as pd

# ==========================
# Load Datasets
# ==========================

customers = pd.read_csv("data/olist_customers_dataset.csv")

orders = pd.read_csv("data/olist_orders_dataset.csv")

order_items = pd.read_csv("data/olist_order_items_dataset.csv")

payments = pd.read_csv("data/olist_order_payments_dataset.csv")

products = pd.read_csv("data/olist_products_dataset.csv")

sellers = pd.read_csv("data/olist_sellers_dataset.csv")

reviews = pd.read_csv("data/olist_order_reviews_dataset.csv")

geolocation = pd.read_csv("data/olist_geolocation_dataset.csv")

translation = pd.read_csv("data/product_category_name_translation.csv")

# ==========================
# Dataset Shapes
# ==========================

print("="*50)
print("DATASET SHAPES")
print("="*50)

print("Customers      :", customers.shape)
print("Orders         :", orders.shape)
print("Order Items    :", order_items.shape)
print("Payments       :", payments.shape)
print("Products       :", products.shape)
print("Sellers        :", sellers.shape)
print("Reviews        :", reviews.shape)
print("Geolocation    :", geolocation.shape)
print("Translation    :", translation.shape)

# ==========================
# Preview
# ==========================

print("\n")
print("="*50)
print("ORDERS DATASET")
print("="*50)

print(orders.head())

print("\n")
print("="*50)
print("CUSTOMERS DATASET")
print("="*50)

print(customers.head())
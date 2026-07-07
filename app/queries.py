import pandas as pd

def monthly_revenue(conn):

    query = """
    SELECT

        strftime('%Y-%m', o.order_purchase_timestamp) AS Month,

        ROUND(SUM(p.payment_value),2) AS Revenue

    FROM orders o

    JOIN payments p

    ON o.order_id = p.order_id

    GROUP BY Month

    ORDER BY Month;

    """

    return pd.read_sql_query(query, conn)
def payment_distribution(conn):

    query = """
    SELECT
        payment_type,
        ROUND(SUM(payment_value),2) AS Revenue
    FROM payments
    GROUP BY payment_type
    ORDER BY Revenue DESC;
    """

    return pd.read_sql_query(query, conn)

def orders_by_state(conn):

    query = """
    SELECT

        c.customer_state,

        COUNT(o.order_id) AS Total_Orders

    FROM orders o

    JOIN customers c

    ON o.customer_id = c.customer_id

    GROUP BY c.customer_state

    ORDER BY Total_Orders DESC

    LIMIT 10;
    """

    return pd.read_sql_query(query, conn)
def top_products(conn):

    query = """
    SELECT

        p.product_category_name,

        COUNT(oi.order_id) AS Total_Sales

    FROM order_items oi

    JOIN products p

    ON oi.product_id = p.product_id

    GROUP BY p.product_category_name

    ORDER BY Total_Sales DESC

    LIMIT 10;
    """

    return pd.read_sql_query(query, conn)

def top_customers(conn):

    query = """
    SELECT

        c.customer_unique_id,

        c.customer_state,

        COUNT(o.order_id) AS Total_Orders,

        ROUND(SUM(p.payment_value),2) AS Total_Spent

    FROM customers c

    JOIN orders o
    ON c.customer_id = o.customer_id

    JOIN payments p
    ON o.order_id = p.order_id

    GROUP BY c.customer_unique_id,
             c.customer_state

    ORDER BY Total_Spent DESC

    LIMIT 10;
    """

    return pd.read_sql_query(query, conn)
def best_payment_method(conn):

    query = """
    SELECT
        payment_type,
        ROUND(SUM(payment_value),2) AS Revenue
    FROM payments
    GROUP BY payment_type
    ORDER BY Revenue DESC
    LIMIT 1;
    """

    return pd.read_sql_query(query, conn)


def top_state(conn):

    query = """
    SELECT
        c.customer_state,
        COUNT(o.order_id) AS Orders
    FROM customers c
    JOIN orders o
        ON c.customer_id = o.customer_id
    GROUP BY c.customer_state
    ORDER BY Orders DESC
    LIMIT 1;
    """

    return pd.read_sql_query(query, conn)


def best_category(conn):

    query = """
    SELECT
        p.product_category_name,
        COUNT(*) AS Sales
    FROM order_items oi
    JOIN products p
        ON oi.product_id = p.product_id
    GROUP BY p.product_category_name
    ORDER BY Sales DESC
    LIMIT 1;
    """

    return pd.read_sql_query(query, conn)


def average_order(conn):

    query = """
    SELECT
        ROUND(AVG(payment_value),2) AS Avg_Order
    FROM payments;
    """

    return pd.read_sql_query(query, conn)
import streamlit as st
import sqlite3
import pandas as pd

from queries import (
    monthly_revenue,
    payment_distribution,
    orders_by_state,
    top_products,
    top_customers,
    best_payment_method,
    top_state,
    best_category,
    average_order
)

from charts import (
    revenue_chart,
    payment_donut,
    state_chart,
    product_chart
)

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="RetailPulse Executive Dashboard",
    page_icon="📊",
    layout="wide"
)

# ==========================================
# DATABASE CONNECTION
# ==========================================

conn = sqlite3.connect("data/ecommerce.db")

# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.image(
        "https://img.icons8.com/fluency/96/combo-chart.png",
        width=80
    )

    st.title("RetailPulse")

    st.caption("Executive Analytics Dashboard")

    st.divider()

    st.subheader("📊 Filters")

    state = st.selectbox(
        "State",
        ["All States"]
    )

    payment = st.selectbox(
        "Payment Type",
        [
            "All",
            "Credit Card",
            "Boleto",
            "Voucher",
            "Debit Card"
        ]
    )

    category = st.selectbox(
        "Category",
        ["All Categories"]
    )

    st.divider()

    st.success("✅ Connected to SQLite")

    st.caption("Version 1.0")

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

.stApp{
    background:#F5F7FA;
}

.big-title{
    font-size:42px;
    font-weight:700;
    color:#1E3A8A;
    margin-bottom:0px;
}

.sub-title{
    color:#6B7280;
    font-size:18px;
    margin-top:-10px;
}

.kpi-card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 4px 15px rgba(0,0,0,0.08);
    border-left:6px solid #2563EB;
}

.kpi-title{
    color:#6B7280;
    font-size:16px;
}

.kpi-value{
    font-size:32px;
    font-weight:bold;
    color:#111827;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# HEADER
# ==========================================
st.caption(
    "Real-time Executive Dashboard for Retail Business Analytics"
)
st.markdown("""
<div class='big-title'>
📊 RetailPulse Executive Dashboard
</div>

<div class='sub-title'>
Business Intelligence Dashboard built using SQL • SQLite • Python • Plotly • Streamlit
</div>
""", unsafe_allow_html=True)

st.divider()

# ==========================================
# KPI QUERIES
# ==========================================

revenue = pd.read_sql_query("""
SELECT ROUND(SUM(payment_value),2) AS Revenue
FROM payments;
""", conn)

orders = pd.read_sql_query("""
SELECT COUNT(*) AS Orders
FROM orders;
""", conn)

customers = pd.read_sql_query("""
SELECT COUNT(*) AS Customers
FROM customers;
""", conn)

products = pd.read_sql_query("""
SELECT COUNT(*) AS Products
FROM products;
""", conn)

avg_order = pd.read_sql_query("""
SELECT ROUND(AVG(payment_value),2) AS AvgOrder
FROM payments;
""", conn)

# ==========================================
# KPI CARDS
# ==========================================

c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    st.markdown(f"""
    <div class='kpi-card'>
        <div class='kpi-title'>💰 Revenue</div>
        <div class='kpi-value'>${revenue.iloc[0,0]:,.2f}</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class='kpi-card'>
        <div class='kpi-title'>📦 Orders</div>
        <div class='kpi-value'>{orders.iloc[0,0]:,}</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class='kpi-card'>
        <div class='kpi-title'>👥 Customers</div>
        <div class='kpi-value'>{customers.iloc[0,0]:,}</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class='kpi-card'>
        <div class='kpi-title'>🛍 Products</div>
        <div class='kpi-value'>{products.iloc[0,0]:,}</div>
    </div>
    """, unsafe_allow_html=True)

with c5:
    st.markdown(f"""
    <div class='kpi-card'>
        <div class='kpi-title'>⭐ Avg Order</div>
        <div class='kpi-value'>${avg_order.iloc[0,0]:,.2f}</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ==========================================
# ANALYTICS CHARTS
# ==========================================

st.divider()

left, right = st.columns(2)

# ---------------------------
# Monthly Revenue Trend
# ---------------------------

with left:

    st.subheader("📈 Monthly Revenue Trend")

    monthly_df = monthly_revenue(conn)

    fig = revenue_chart(monthly_df)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ---------------------------
# Payment Distribution
# ---------------------------

...
with right:

    st.subheader("🍩 Payment Method Distribution")

    payment_df = payment_distribution(conn)

    fig = payment_donut(payment_df)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =====================================
# SECOND ROW
# =====================================

st.divider()

left, right = st.columns(2)

# Orders by State

with left:

    st.subheader("🌍 Orders by State")

    state_df = orders_by_state(conn)

    fig = state_chart(state_df)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# Top Product Categories
# Top Product Categories

with right:

    st.subheader("🏆 Top Product Categories")

    product_df = top_products(conn)

    fig = product_chart(product_df)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ==========================================
# TOP CUSTOMERS
# ==========================================

st.divider()

st.subheader("👥 Top 10 Customers")

customer_df = top_customers(conn)

st.dataframe(
    customer_df,
    use_container_width=True,
    hide_index=True
)

# ==========================================
# EXECUTIVE INSIGHTS
# ==========================================

st.divider()

st.subheader("📋 Executive Insights")

payment = best_payment_method(conn)
state = top_state(conn)
category = best_category(conn)
avg = average_order(conn)

col1, col2 = st.columns(2)

with col1:

    st.success(f"""
### 💼 Business Highlights

- 💰 Total Revenue exceeded **$16 Million**

- 💳 Best Payment Method:
**{payment.iloc[0,0]}**

- 🌍 Top Performing State:
**{state.iloc[0,0]}**

""")

with col2:

    st.info(f"""
### 📊 Key Metrics

- 🏆 Best Selling Category:
**{category.iloc[0,0]}**

- ⭐ Average Order Value:
**${avg.iloc[0,0]}**

- 📦 Total Orders:
**99,441**

""")


# ==========================================
# EXECUTIVE INSIGHTS
# ==========================================

st.divider()

st.subheader("📋 Executive Insights")

payment = best_payment_method(conn)
state = top_state(conn)
category = best_category(conn)
avg = average_order(conn)

col1, col2 = st.columns(2)

with col1:
    st.success(f"""
### 💼 Business Highlights

- 💰 Revenue exceeded **$16 Million**
- 💳 Best Payment Method: **{payment.iloc[0,0]}**
- 🌍 Top Performing State: **{state.iloc[0,0]}**
""")

with col2:
    st.info(f"""
### 📊 Key Metrics

- 🏆 Best Selling Category: **{category.iloc[0,0]}**
- ⭐ Average Order Value: **${avg.iloc[0,0]}**
- 📦 Total Orders: **99,441**
""")
    
st.divider()

st.caption(
    "RetailPulse Executive Dashboard | Built with SQLite, SQL, Python, Plotly & Streamlit"
)    

st.divider()

st.markdown("""
<center>

Built with  using

<b>Python • SQLite • Plotly • Streamlit</b>

</center>
""", unsafe_allow_html=True)
conn.close()
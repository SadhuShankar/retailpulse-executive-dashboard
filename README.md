# 📊 RetailPulse Executive Dashboard

## 📌 Overview
RetailPulse is a Business Intelligence dashboard built using SQL, SQLite, Python, Plotly, and Streamlit. It provides interactive analytics on an e-commerce dataset, enabling business users to monitor revenue, customer behavior, payment trends, and product performance.

---

## 🚀 Features

- 📈 Monthly Revenue Trend
- 🍩 Payment Method Distribution
- 🌍 Orders by State
- 🏆 Top Product Categories
- 👥 Top Customers
- 📊 KPI Cards
- 📋 Executive Insights
- 🎨 Interactive Streamlit Dashboard

---

## 🛠 Tech Stack

- Python
- SQL
- SQLite
- Pandas
- Plotly
- Streamlit

---

## 📂 Project Structure

RetailPulse/
│
├── app/
│ ├── app.py
│ ├── queries.py
│ └── charts.py
│
├── data/
│ └── ecommerce.db
│
├── reports/
│ └── screenshots/
│
├── sql/
│ └── queries.sql
│
├── requirements.txt
└── README.md

---

## 📸 Dashboard Screenshots

### Dashboard Overview

![Dashboard](reports/screenshots/dashboard.png)

### Revenue & Payment Analytics

![Revenue](reports/screenshots/revenue.png)

### State & Product Analytics

![State](reports/screenshots/state.png)

### Executive Insights

![Insights](reports/screenshots/insights.png)

---

## ▶️ Run Locally

```bash
git clone <repository-url>

cd RetailPulse

pip install -r requirements.txt

streamlit run app/app.py

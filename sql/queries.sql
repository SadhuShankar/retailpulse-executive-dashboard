-- =====================================
-- Query 1
-- Total Orders
-- =====================================

SELECT COUNT(*) AS Total_Orders
FROM orders;

-- =====================================
-- Query 2
-- Total Revenue
-- =====================================

SELECT
    ROUND(SUM(payment_value), 2) AS Total_Revenue
FROM payments;

-- =====================================
-- Query 3
-- Average Order Value
-- =====================================

SELECT
    ROUND(AVG(payment_value), 2) AS Average_Order_Value
FROM payments;

-- =====================================
-- Query 4
-- Maximum Payment
-- =====================================

SELECT
    MAX(payment_value) AS Highest_Payment
FROM payments;

-- =====================================
-- Query 6
-- Revenue by Payment Type
-- =====================================

SELECT
    payment_type,
    ROUND(SUM(payment_value),2) AS Revenue
FROM payments
GROUP BY payment_type;

-- =====================================
-- Query 7
-- Revenue by Payment Type (Descending)
-- =====================================

SELECT
    payment_type,
    ROUND(SUM(payment_value),2) AS Revenue
FROM payments
GROUP BY payment_type
ORDER BY Revenue DESC;

-- =====================================
-- Query 8
-- Orders by State
-- =====================================

SELECT
    c.customer_state,
    COUNT(o.order_id) AS Total_Orders
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_state
ORDER BY Total_Orders DESC;

-- =====================================
-- Query 9
-- States with More Than 3000 Orders
-- =====================================

SELECT
    c.customer_state,
    COUNT(o.order_id) AS Total_Orders
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_state
HAVING COUNT(o.order_id) > 3000
ORDER BY Total_Orders DESC;

-- =====================================
-- Query 10
-- Payment Category
-- =====================================

SELECT
    payment_value,

    CASE
        WHEN payment_value > 500 THEN 'High Value'
        WHEN payment_value > 100 THEN 'Medium Value'
        ELSE 'Low Value'
    END AS Payment_Category

FROM payments

LIMIT 20;

-- =====================================
-- Query 11
-- Customers Without Orders
-- =====================================

SELECT
    COUNT(*) AS Customers_Without_Orders
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;

-- =====================================
-- Query 12
-- Payments Above Average
-- =====================================

SELECT
    payment_value
FROM payments
WHERE payment_value >
(
    SELECT AVG(payment_value)
    FROM payments
)
ORDER BY payment_value DESC
LIMIT 20;

-- =====================================
-- Query 13
-- CTE Example
-- Revenue by Payment Type
-- =====================================

WITH PaymentRevenue AS
(
    SELECT
        payment_type,
        ROUND(SUM(payment_value),2) AS Revenue
    FROM payments
    GROUP BY payment_type
)

SELECT *
FROM PaymentRevenue
WHERE Revenue > 500000
ORDER BY Revenue DESC;

-- =====================================
-- Query 14
-- Rank Payment Types by Revenue
-- =====================================

SELECT
    payment_type,
    ROUND(SUM(payment_value),2) AS Revenue,

    RANK() OVER(
        ORDER BY SUM(payment_value) DESC
    ) AS Revenue_Rank

FROM payments

GROUP BY payment_type;

-- =====================================
-- Query 15
-- Dense Rank Payment Types
-- =====================================

SELECT
    payment_type,
    ROUND(SUM(payment_value),2) AS Revenue,

    DENSE_RANK() OVER(
        ORDER BY SUM(payment_value) DESC
    ) AS Dense_Rank

FROM payments

GROUP BY payment_type;

-- =====================================
-- Query 16
-- Row Number
-- =====================================

SELECT
    payment_type,
    ROUND(SUM(payment_value),2) AS Revenue,

    ROW_NUMBER() OVER(
        ORDER BY SUM(payment_value) DESC
    ) AS Row_Number

FROM payments

GROUP BY payment_type;

-- =====================================
-- Query 17
-- Top 3 Payment Methods
-- =====================================

WITH RevenueRank AS
(
    SELECT
        payment_type,
        ROUND(SUM(payment_value),2) AS Revenue,

        RANK() OVER(
            ORDER BY SUM(payment_value) DESC
        ) AS Rank_No

    FROM payments

    GROUP BY payment_type
)

SELECT *

FROM RevenueRank

WHERE Rank_No <= 3;
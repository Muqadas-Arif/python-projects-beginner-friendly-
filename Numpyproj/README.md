“Synthetic Retail Sales Analysis.”

Over a Jupyter Notebook, I generated a realistic synthetic sales dataset (200 orders for Jan 2026) containing product IDs, categories (Electronics, Apparel, Grocery), quantities, unit prices, discounts, order dates, and store IDs — then used NumPy for fast, vectorized analysis.

What I did

Built a structured NumPy dataset and computed derived fields (total price, final price after discounts).
Performed exploratory analysis: order counts by category, top-selling products by quantity, and average order value (~9,194).
Aggregated revenue per store (Store 2 and Store 3 were among the highest), identified highest-revenue dates (e.g., 2026-01-15 ≈ 174,308.85), and detected high-value orders.
Applied data transformations: normalization, revenue bucketing (Low/Medium/High), and created simple business rules (e.g., conditional bonuses).
Answered operational questions like how many orders had discounts (157), average quantities for discounted orders by category, and product distribution across stores.
Why it matters

Shows how compact, vectorized NumPy workflows can power fast EDA and simple revenue analytics.
Useful as a hands-on demo for retail analytics concepts: revenue aggregation, discount impact, date-based trends, and identifying high-value customers/orders.
Tech: Python, NumPy, Jupyter Notebook

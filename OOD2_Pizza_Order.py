"""
Design the core object-oriented model for a pizza ordering system used by a small restaurant. The system should allow customers to:

- browse a menu of pizzas,
- customize each pizza by size, crust, and toppings,
- place an order containing one or more pizzas,
- calculate item prices and the final order total,
- choose pickup or delivery,
- pay using different payment methods,
- track order status such as placed, preparing, baking, ready, and delivered.
"""

"""
Clarification
1. core requirements
2. edge cases / error handling
3. out of scope
"""

"""
FR:
1. Menu Browsing — The system must display a list of available pizzas, including name, description, base ingredients, and base price.

2. Pizza Customization — Customers must be able to choose size (S/M/L), crust type (thin, regular, deep dish), and add/remove toppings.

3. Order Creation — Customers must be able to add one or more customized pizzas to a cart and submit an order.

4. Price Calculation — The system must compute each pizza’s price based on size, crust, and toppings, then compute tax and final total.

5. Pickup_or_Delivery — Customers must choose between pickup or delivery; delivery requires address entry and delivery fee calculation.

6. Payment Processing — Support multiple payment methods (cash, card, digital wallet). Payment status must be tracked.

7. Order Status Tracking — The system must support status transitions: Placed → Preparing → Baking → Ready → Delivered.

Edge cases:
1. Payment Failure — Declined card, expired card, or interrupted payment must allow retry or switching payment method.

2. Invalid Customization — Selecting incompatible toppings (e.g., unavailable items) must show an error.

Out of Scope:
1. User Notifications — Notify customers when order status changes (SMS, email, or in‑app).

2. Operational Dashboard — Staff must be able to view incoming orders, update status, and mark items as completed.

3. Receipts_and_Summaries — Generate an order summary with itemized pricing, taxes, fees, and payment confirmation. 

4. Third‑Party Delivery Integration — No integration with UberEats, DoorDash, etc.

5. Complex Tax Rules — Only simple flat tax; no multi‑jurisdiction tax logic.

6. Customer Accounts — No login system; orders are guest-based unless explicitly added later.

7. Inventory Management — No automated stock tracking or forecasting.
"""
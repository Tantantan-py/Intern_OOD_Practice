"""
Design an Object-Oriented Shopping Cart
Design the core objects and interfaces for a shopping cart. It must add, remove, and change item quantities; calculate a subtotal; apply independently evolving pricing adjustments; and expose a stable summary for checkout. Focus on responsibilities, invariants, and how new rules can be introduced without rewriting the cart.

Constraints & Assumptions
Product IDs are stable, but display metadata may change outside the cart.
Monetary arithmetic uses an exact decimal or integer minor-unit type.
A cart line has a positive quantity and a captured unit price or pricing reference.
Inventory reservation and payment execution are outside the initial object boundary.
Promotions may reject or adjust selected lines but must be explainable.


Part 1 - Domain model and invariants
Define cart, line item, money, product/pricing reference, and summary objects. Identify which object owns quantity and subtotal invariants.

Part 2 - Extensible pricing behavior
Design a pricing or adjustment interface for coupons, item discounts, and future rules without adding conditionals throughout the cart.

Part 3 - Persistence and testing
Explain optimistic concurrency, idempotent commands, serialization, and tests for interacting changes.
"""
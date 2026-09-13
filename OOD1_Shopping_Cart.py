"""
Design an Object-Oriented Shopping Cart
The Cart object is a simple container that manages items, quantities, and subtotal calculation. It supports adding, removing, and updating items, and it allows pricing adjustments to modify the subtotal or unit prices. It acts as the central object coordinating cart state and pricing changes.
"""

class Cart:
    def __init__(self):
        self.items = {}
        self.subtotal = 0.0

    def add_item(self, product_id, quantity, unit_price):
        if product_id in self.items:
            self.items[product_id]['quantity'] += quantity
        else:
            self.items[product_id] = {'quantity': quantity, 'unit_price': unit_price}
        self.update_subtotal()

    def remove_item(self, product_id):
        if product_id in self.items:
            del self.items[product_id]
            self.update_subtotal()

    def change_quantity(self, product_id, new_quantity):
        if product_id in self.items and new_quantity > 0:
            self.items[product_id]['quantity'] = new_quantity
            self.update_subtotal()
        elif new_quantity <= 0:
            self.remove_item(product_id)

    def update_subtotal(self):
        self.subtotal = sum(item['quantity'] * item['unit_price'] for item in self.items.values())


class Item:
    def __init__(self, product_id, quantity, unit_price):
        self.product_id = product_id
        self.quantity = quantity
        self.unit_price = unit_price


class pricingAdjustment:
    def apply(self, cart):
        raise NotImplementedError("Subclasses should implement this method.")


class Coupon(pricingAdjustment):
    def __init__(self, discount_amount):
        self.discount_amount = discount_amount

    def apply(self, cart):
        cart.subtotal -= self.discount_amount
        if cart.subtotal < 0:
            cart.subtotal = 0.0


class ItemDiscount(pricingAdjustment):
    def __init__(self, product_id, discount_amount):
        self.product_id = product_id
        self.discount_amount = discount_amount

    def apply(self, cart):
        if self.product_id in cart.items:
            item = cart.items[self.product_id]
            item['unit_price'] -= self.discount_amount
            if item['unit_price'] < 0:
                item['unit_price'] = 0.0
            cart.update_subtotal()
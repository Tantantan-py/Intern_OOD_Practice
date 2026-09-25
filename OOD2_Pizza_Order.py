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

from enum import Enum
from pydantic import BaseModel, Field, field_validator


class Size(str, Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"


class Crust(str, Enum):
    THIN = "thin"
    REGULAR = "regular"
    DEEP_DISH = "deep_dish"


class OrderStatus(str, Enum):
    PLACED = "placed"
    PREPARING = "preparing"
    BAKING = "baking"
    READY = "ready"
    DELIVERED = "delivered"


class OrderType(str, Enum):
    PICKUP = "pickup"
    DELIVERY = "delivery"


class PaymentMethod(str, Enum):
    CASH = "cash"
    CARD = "card"
    DIGITAL_WALLET = "digital_wallet"


class PaymentStatus(str, Enum):
    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"


class Ingredient(BaseModel):
    name: str


class Topping(BaseModel):
    name: str
    price: float = Field(ge=0)
    is_available: bool = True


class Pizza(BaseModel):
    name: str
    description: str
    base_ingredients: List[Ingredient]
    base_price: float = Field(ge=0)


class CustomizedPizza(BaseModel):
    menu_pizza: Pizza
    size: Size
    crust: Crust
    toppings: List[Topping] = []

    @field_validator("toppings")
    def validate_toppings(cls, toppings):
        unavailable = [t.name for t in toppings if not t.is_available]
        if unavailable:
            raise ValueError(f"Unavailable toppings: {', '.join(unavailable)}")
        return toppings


class OrderItem(BaseModel):
    pizza: CustomizedPizza
    quantity: int = Field(gt=0)


class Address(BaseModel):
    street: str
    city: str
    zip: str


class Payment(BaseModel):
    method: PaymentMethod
    status: PaymentStatus = PaymentStatus.PENDING
    amount: float = Field(ge=0)


class Order(BaseModel):
    items: List[OrderItem]
    order_type: OrderType
    delivery_address: Optional[Address] = None
    status: OrderStatus = OrderStatus.PLACED
    payment: Optional[Payment] = None

    @field_validator("delivery_address")
    def validate_delivery(cls, addr, info):
        if info.data["order_type"] == OrderType.DELIVERY and addr is None:
            raise ValueError("Delivery address required for delivery orders.")
        return addr

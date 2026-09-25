"""
Design a pizza order application
order, price calculation
how to select the pizza
caculate the pizza base on size, category or toppings
"""
"""
1. Clarification
 - core requirement
 - edge cases / error handling
 - out of scope

FR:
1. Pizza class - name, size, toppings
2. Prebuild Pizza - preset topping 
3. Custmozed Pizza - set_size, add_topping, set_name, remove_topping
4. Order - user_name, pizzas; add_pizza, summary (print), checkout
"""
"""
Follow ups:
Coupon
"""


# from enum import Enum


# class Size(str, Enum):
#     SMALL = "small"
#     MEDIUM = "medium"
#     LARGE = "large"


"""
1. Enum
2. Entities
3. Service / method impl
"""
SIZE_PRICE = {"s": 8, "m": 10, "l": 12}
PRESET_TOPPINGS = {
    "perpperoni": ["perpperoni"],
    "veggi": ["onion", "pepper"]
}
VALID_SIZES = SIZE_PRICE.keys()

class Pizza:
    def __init__(self, name, size, topping = None, price_strategy= None):
        self.name = name
        self.size = size
        self.topping = topping if topping else []
        self.price_strategy = price_strategy or DefaultPricing()

    def calculate_price(self):
        return self.price_strategy.calculate(self)


    def __str__(self):
        return f"{self.size} {self.name} Pizza with {','.join(self.topping)}"


# Factory Pattern
class PizzaFactroy:
    @staticmethod
    def create_pizza(size, category):
        name = category
        if name not in PRESET_TOPPINGS:
            raise ValueError(f"Not Impl")

        return Pizza(name=name, size=size, topping=PRESET_TOPPINGS[name])

# Customized Pizza - Builder Pattern
class PizzaBuilder:
    def __init__(self):
        self.name = "custom"
        self.size = "l"
        self.topping = []

    def set_size(self, new_size: str):
        new_size = new_size
        if new_size not in ["s", "m", "l"]: # not in VALID_SIZES; SIZE_PRICE.keys()
            raise ValueError(f"UNKNOWN SIZE")
        self.size = new_size
        return self

    def set_name(self, new_name):
        pass

    def add_topping(self, topping):
        self.topping.append(topping)
        return self

    # error handling -> removing non exisiting topping

    def build(self):
        return Pizza(name=self.name, size=self.size, topping=self.topping)

    # how to build from another pizza
    @classmethod
    def from_pizza(cls, pizza: Pizza):
        builder = cls()
        builder.set_name(pizza.name)
        builder.set_size(pizza.size)
        builder.topping = pizza.topping.copy()
        return builder


class Order:
    def __init__(self, user_name):
        self.user_name = user_name
        self.pizzas= []

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def get_summary(self):
        for i, pizza in enumerate(self.pizzas):
            print(f"Pizza {i+1}. {pizza.name} - Price: ${pizza.calculate_price()}")


# Strategy Pattern
from abc import ABC, abstractmethod


class PriceStrategy(ABC):
    @abstractmethod
    def calculate(self, pizza):
        pass

class DefaultPricing(PriceStrategy):
    def calculate(self, pizza):
        base = SIZE_PRICE.get(pizza.size)
        total = base + len(pizza.topping) * 1.2

        return total

class LargePizzaDiscount(PriceStrategy):
    def calculate(self, pizza):
        base = SIZE_PRICE.get(pizza.size)
        discount = LARGE_PIZZA_PROMNOTION if pizza.size = "l" else 0
        return base + len(pizza.topping) * 1.2 - discount

    
order = Order("lucian")
pizza1 = PizzaFactroy.create_pizza("l", "pepperoni")
pizza1.price_strategy = LargePizzaDiscount()
order.add_pizza(pizza1)

pizza2 = PizzaBuilder().set_name("lucian's custom").set_size("m").add.topping("onion").build()

pizza2.remove_topping("pepper")
order.add_pizza(pizza2)


class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        if not isinstance(name, str) or not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Invalid item name or price")
        if name in self.items:
            self.items[name] += price
        else:
            self.items[name] = price

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
        else:
            raise KeyError(f"Item '{name}' not found in cart")

    def total_cost(self):
        return sum(self.items.values())

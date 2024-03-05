class CashRegister:
    def __init__(self, discount=0, total=0, items=None):
        self.discount = discount
        self.total = total
        self.items = items if items is not None else []

    def register_totals(self):
        return self.total

    def discount_attribute(self):
        return self.discount

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(title)
        return self.total

    def apply_discount(self):
        self.total *= 0.8  
        return self.total

    def apply_discount_success_message(self):
        discounted_total = self.apply_discount()
        return f"After the discount, the total comes to ${discounted_total}.\n"

    def discount_when_no_discount(self):
        if self.discount == 0:
            return 'There is no discount to apply.\n'

    def list_items(self):
        return self.items

    def void_last_transaction(self):
        if self.items:
            last_item = self.items.pop()
            self.total -= last_item[1] * last_item[2]  
            return self.total

    def reset_total(self):
        self.total = 0
        self.items = []


new = CashRegister()
new.add_item("macbook air", 1000, 2)
print(new.apply_discount_success_message())

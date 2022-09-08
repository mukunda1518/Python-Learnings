class Cart:

    def __init__(self):
        self.items = {}
        self.price_details = {"Book": 100, "Laptop": 50000}

    def add_items(self, item_name, quantity):
        self.items[item_name] = quantity

    def remove_item(self, item_name):
        del self.items[item_name]

    def update_quantity(self, item_name, quantity):
        self.items[item_name] = quantity

    def get_items(self):
        item_list = list(self.items.keys())
        print(item_list)

    def get_total_price(self):
        total_price = 0
        for item_name, quantity in self.items.items():
            total_price += self.price_details[item_name] * quantity
        return total_price


cart_obj = Cart()
cart_obj.add_items("Book", 10)
cart_obj.get_items()
cart_obj.add_items("Laptop", 2)
cart_obj.get_items()
cart_obj.remove_item("Book")
cart_obj.get_items()
cart_obj.update_quantity("Laptop", 1)
cart_obj.get_items()
print(cart_obj.get_total_price())


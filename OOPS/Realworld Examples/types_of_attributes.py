
# Attributes values changes for each instance are called Instance attributes
# Attributes values are common for all instance are called Class Attributes
# self is nothing but instance there - obj and self are referring to same id in memory

class Cart:
    flat_discount = 0
    min_bill = 100

    def __init__(self):
        self.items = {}

    def add_items(self, item_name, quantity):
        self.items[item_name] = quantity

    def display_items(self):
        print(self)
        print(self.items)

    def print_min_bill(self):
        print(Cart.min_bill)


cart_obj = Cart()
cart_obj.add_items("Book", 10)
print(cart_obj)   # Same
cart_obj.display_items()   # Same
print(cart_obj.items)   # Accessing like this is not a best practice, so use methods

print(Cart.min_bill)  # Accessing class attribute
cart_obj.print_min_bill()

cart_obj1 = Cart()
cart_obj1.print_min_bill()

Cart.min_bill = 200

cart_obj.print_min_bill()
cart_obj1.print_min_bill()


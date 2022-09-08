# Instance Methods
# Instance methods can access all attributes of the instance and have self as a parameter.

# Class Methods
# Methods which need access to class attributes but not instance attributes are marked as Class Methods.
# For class methods, we send cls as a parameter indicating we are passing the class.


# Static Method
# We might need some generic methods that don’t need access to either instance or class attributes. These type of methods are called Static Methods.
# Usually, static methods are used to create utility functions which make more sense to be part of the class.

class Cart:
    flat_discount = 0
    min_bill = 100

    def __init__(self):
        self.items = {}

    def add_items(self, item_name, quantity):
        self.items[item_name] = quantity
        self.display_items()

    def display_items(self):
        print(self.items)

    @classmethod
    def update_flat_discount(cls, new_flat_discount):
        cls.flat_discount = new_flat_discount

    @classmethod
    def increase_flat_discount(cls, amount):
        new_flat_discount = cls.flat_discount + amount
        cls.update_flat_discount(new_flat_discount)

    @staticmethod
    def greet():
        print("Have a Great Shopping")


# Instance Methods
cart_obj = Cart()
cart_obj.add_items("Book", 10)
cart_obj.display_items()

# Class Methods
print(Cart.flat_discount)
Cart.update_flat_discount(20)
print(Cart.flat_discount)
Cart.increase_flat_discount(100)
print(Cart.flat_discount)

# Static Method
Cart.greet()
cart_obj.greet()


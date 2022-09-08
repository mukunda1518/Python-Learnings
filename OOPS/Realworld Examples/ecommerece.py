# Polymorphism - https://www.programiz.com/python-programming/polymorphism

class Product:
    def __init__(self, name, price, deal_price, rating):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.rating = rating
        self.you_save = price - deal_price

    def display_product_details(self):
        print("Product name: {}".format(self.name))
        print("Price: {}".format(self.price))
        print("Deal price: {}".format(self.deal_price))
        print("Rating: {}".format(self.rating))
        print("You save: {}".format(self.you_save))

    def get_deal_price(self):
        return self.deal_price


class ElectronicItem(Product):

    def __init__(self, name, price, deal_price, rating, warranty_in_months):
        super().__init__(name, price, deal_price, rating)
        self.warranty_in_months = warranty_in_months

    def display_product_details(self):
        super().display_product_details()
        print("Warranty in months: {}".format(self.warranty_in_months))


class Laptop(ElectronicItem):

    def __init__(self, name, price, deal_price, rating, warranty_in_months, ram, storage):
        super().__init__(name, price, deal_price, rating, warranty_in_months)
        self.ram = ram
        self.storage = storage

    def display_product_details(self):
        super().display_product_details()
        print("Ram: {}".format(self.ram))
        print("Storage: {}".format(self.storage))


class GroceryItem(Product):

    def __init__(self, name, price, deal_price, rating, expiry_date):
        super().__init__(name, price, deal_price, rating)
        self.expiry_date = expiry_date

    def display_product_details(self):
        super().display_product_details()
        print("Expiry Date: {}".format(self.expiry_date))


class Order:

    delivery_charges = {
        "Normal": 0,
        "Prime Delivery": 100
    }

    def __init__(self, delivery_method, delivery_address):
        self.items_in_cart = []
        self.delivery_method = delivery_method
        self.delivery_address = delivery_address

    def add_item(self, product, quantity):
        item = (product, quantity)
        self.items_in_cart.append(item)

    def display_order_details(self):
        print("Delivery Method: {}".format(self.delivery_method))
        print("Delivery Address: {}".format(self.delivery_address))
        print("-" * 5, "products", "-" * 5)
        for product, quantity in self.items_in_cart:
            product.display_product_details()
            print("Quantity: {}".format(quantity))
            print()
        total_bill = self.get_total_bill()
        print("Total Bill: {}".format(total_bill))
        print("-" * 15)

    def get_total_bill(self):
        total_bill = 0
        for product, quantity in self.items_in_cart:
            price = product.get_deal_price() * quantity
            total_bill += price
        order_delivery_charges = Order.delivery_charges[self.delivery_method]
        total_bill += order_delivery_charges
        return total_bill

    @classmethod
    def update_delivery_charges(cls, delivery_method, charges):
        cls.delivery_charges[delivery_method] = charges


tv = ElectronicItem("TV", 25000, 15000, 3.4, 24)
milk = GroceryItem("Milk", 40, 30, 4.6, "Jan 2020")
my_order = Order("Normal", "Hyderabad")
my_order.add_item(tv, 1)
my_order.add_item(milk, 3)
my_order.display_order_details()

Order.update_delivery_charges("Normal", 10)
my_order.display_order_details()

lenovo_lap = Laptop("Lenovo", 45000, 30000, 4.5, 24, "16 GB", "1 TB SSD")
lenovo_lap.display_product_details()

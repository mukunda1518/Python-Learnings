# Composition
# Modelling instances of one class as attributes of another class is called Composition

# Overriding methods

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


class Order:

    def __init__(self, delivery_speed, delivery_address):
        self.items_in_cart = []
        self.delivery_speed = delivery_speed
        self.delivery_address = delivery_address

    def add_item(self, product, quantity):
        self.items_in_cart.append((product, quantity))

    def display_order_details(self):
        for product, quantity in self.items_in_cart:
            product.display_product_details()
            print("Quantity: {}".format(quantity))
            print()

    def get_total_bill(self):
        total_bill = 0
        for product, quantity in self.items_in_cart:
            price = product.get_deal_price() * quantity
            total_bill += price
        print("Total Bill: {}".format(total_bill))


class GroceryItem(Product):

    def __init__(self, name, price, deal_price, rating, expiry_date):
        super().__init__(name, price, deal_price, rating)
        self.expiry_date = expiry_date

    def display_product_details(self):
        super().display_product_details()
        print("Expiry Date: {}".format(self.expiry_date))


tv = ElectronicItem("TV", 20000, 15000, 3.5, 5)

milk = GroceryItem("Milk", 40, 25, 4, "2024-09-12")

order_obj = Order("Prime Delivery", "Hyderabad")
order_obj.add_item(tv, 1)
order_obj.add_item(milk, 10)

order_obj.display_order_details()
order_obj.get_total_bill()

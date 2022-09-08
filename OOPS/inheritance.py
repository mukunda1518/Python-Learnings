# Through Inheritance Resuability, Clear Separation, More Organised  can be achieved
import datetime


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


class ElectronicItem(Product):

    def display_electronic_item_details(self):
        self.display_product_details()
        print("Warranty in months: {}".format(self.warranty_in_months))

    def set_warranty(self, warranty_in_months):
        self.warranty_in_months = warranty_in_months

    def get_warranty(self):
        return self.warranty_in_months


class GroceryItem(Product):

    def set_expiry_date(self, expiry_date):
        self.expiry_date = expiry_date

    def get_expiry_date(self):
        return self.expiry_date


prod1 = Product("Shoes", 500, 250, 3.5)
prod1.display_product_details()
print("-------" * 5)

e_item = ElectronicItem("Camera", 30000, 1000, 4)
e_item.display_product_details()
e_item.set_warranty(24)
print(e_item.get_warranty())
e_item.display_electronic_item_details()


print("-------" * 5)
g_item = GroceryItem("milk", 300, 50, 4)
g_item.display_product_details()
g_item.set_expiry_date(datetime.datetime.now())
print(g_item.get_expiry_date())
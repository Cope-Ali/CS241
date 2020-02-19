from product import Product

class Order():
    """ Order class containing id, products and methods: get_subtotal(), 
    get_tax(), get_total(), add_product(product), display_receipt()"""
    def __init__(self):
        self.id = ""
        self.products = []

    def get_subtotal(self):
        sum = 0
        for p in range(0, len(self.products)):
            sum = sum + self.products[p].get_total_price()
        return sum

    def get_tax(self):
        return self.get_subtotal() * 0.065

    def get_total(self):
        return self.get_subtotal() + self.get_tax()

    def add_product(self, product):
        self.products.append(product)

    def display_receipt(self):
        print("Order: {}".format(self.id))
        for p in range(0, len(self.products)):
            self.products[p].display()
        print("Subtotal: ${:.2f}".format(self.get_subtotal()))
        print("Tax: ${:.2f}".format(self.get_tax()))
        print("Total: ${:.2f}".format(self.get_total()))
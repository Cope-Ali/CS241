from order import Order
class Customer():
    """Customer class contains id, name, orders and methods get_order_count(), 
    get_total(), add_order(order), display_summary(), display_receipts()"""

    def __init__(self):
        self.id=""
        self.name=""
        self.orders= []

    def get_order_count(self):
        return len(self.orders)

    def get_total(self):
        total = 0
        for p in range(0, len(self.orders)):
            total = total + self.orders[p].get_total()
        return total

    def add_order(self, order):
        self.orders.append(order)

    def display_summary(self):
        print("Summary for customer '{}':".format(self.id))
        print("Name: {}".format(self.name))
        print("Orders: {}".format(self.get_order_count()))
        print("Total: ${:.2f}".format(self.get_total()))

    def display_receipts(self):
        print("Detailed receipts for customer '{}':".format(self.id))
        print("Name: {}".format(self.name))
        for i in range(0, len(self.orders)):
            print("")
            self.orders[i].display_receipt()


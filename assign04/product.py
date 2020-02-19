class Product():
    """Product class containing attributes: id, name, price, quantity 
    and methods:get_total_price(), display()"""
    def __init__(self, idNum, name, price, quant):
        self.id = idNum
        self.name = name 
        self.price = float(price)
        self.quantity = int(quant)

    def get_total_price(self):
        return self.price * self.quantity

    def display(self):
        print("{} ({}) - ${:.2f}".format(self.name, self.quantity, self.get_total_price()))
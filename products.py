class Product:

    def __init__(self, name, price, quantity):
        if not name:
            raise NameError("Name cannot be empty")
        else:
            self.name = name
        if price < 0 or quantity < 0:
            raise ValueError("Price/Quantity cannot be negative")
        else:
            self.price = float(price)
            self.quantity = quantity
        if self.name and self.price and self.quantity:
            self.active = True


    def get_quantity(self):
        return self.quantity


    def set_quantity(self, quantity):
        self.quantity += quantity


    def is_active(self):
        return self.active


    def activate(self):
        self.active = True


    def deactivate(self):
        self.active = False


    def show(self):
        if self.active:
            return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"


    def buy(self, quantity):
        if (self.quantity - quantity) < 0:
            raise ValueError("Cannot buy a higher quantity then the quantity of the item")
        else:
            self.quantity -= quantity
            if self.quantity == 0:
                self.deactivate()
            return self.price * quantity

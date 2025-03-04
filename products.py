class Product:

    def __init__(self, name, price, quantity):
        if not name:
            raise NameError("Name cannot be empty")
        elif not isinstance(price, (float, int)):
            raise TypeError(f"Price has to be a number: {price}")
        elif not isinstance(quantity, int):
            raise TypeError(f"Quantity has to be a whole number: {quantity}")
        elif price < 0 or quantity < 0:
            raise ValueError("Price/Quantity cannot be negative")
        else:
            self.name = name
            self.price = float(price)
            self.quantity = quantity
            self.active = True


    def get_quantity(self):
        return self.quantity


    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()


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
        if not self.is_active():
            raise ValueError("Product Inactive")
        if (self.get_quantity() - quantity) < 0:
            raise ValueError("Quantity larger then what exists")
        else:
            self.set_quantity((self.get_quantity() - quantity))
            return self.price * quantity

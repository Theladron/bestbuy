import products

class Store:

    def __init__(self, product_list):
        self.products = []
        for product in product_list:
            self.products.append(product)


    def add_product(self, product):
        self.products.append(product)


    def remove_product(self, product):
        self.products.remove(product)


    def get_total_quantity(self):
        total_products = 0
        for product in self.products:
            total_products += product.get_quantity()
        return f"Total of {total_products} items in store"


    def get_all_products(self):
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products


    def order(self, shopping_list):
        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return f"Total order price: {total_price}"

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
        self.total_products = 0
        for product in self.products:
            self.total_products += product.get_quantity()
        return f"Total of {self.total_products} items in store"


    def get_all_products(self):
        self.active_products = []
        for product in self.products:
            if product.is_active():
                self.active_products.append(product)
        return self.active_products


    def order(self, shopping_list):
        self.total_price = 0
        for product, quantity in shopping_list:
            self.total_price += product.buy(quantity)
        return f"Total order price: {self.total_price}"


product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
               ]

best_buy = Store(product_list)
products = best_buy.get_all_products()
print(best_buy.get_total_quantity())
print(best_buy.order([(products[0], 1), (products[1], 2)]))
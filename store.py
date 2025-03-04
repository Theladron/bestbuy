class Store:

    def __init__(self, product_list):
        self.products = []
        for product in product_list:
            self.add_product(product)


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
        return self.products



    def order(self, shopping_list):
        total_price = 0
        for product, quantity in shopping_list:
            try:
                total_price += product.buy(quantity)
                if not product.is_active():
                    self.remove_product(product)
            except ValueError as e:
                return (f"Error while making order: {e}.\n"
                        f"Total order price before the error occurred: {total_price}")

        return f"Total order price: {total_price}"

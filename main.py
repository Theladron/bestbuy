import store
import products

def show_current_stock(shop):
    print(shop.get_total_quantity())


def show_products(shop):
    product_list = shop.get_all_products()
    for index in range(len(product_list)):
        print(f"{index+1}. {product_list[index].show()}")


def make_order(shop):
    show_products(shop)
    product_list = shop.get_all_products()
    print("When you want to finish order, enter empty text.")
    order_list = []
    while True:
        item = int(input("Which product # do you want? "))
        quantity = int(input("What amount do you want? "))
        if isinstance(item and quantity, int):
            order_list.append((product_list[item-1], quantity))
            print(shop.order(order_list))
        else:
            break


def start(shop):
    menu_funct = {1: show_products,
                  2: show_current_stock,
                  3: make_order,
                  }
    while True:

        print("""1. List all products in store
    2. Show total amount in store
    3. Make an order
    4. Quit""")
        user_input = int(input("Enter a number: "))
        if user_input == 4:
            exit()
        else:
            menu_funct[user_input](shop)


def main():

    product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
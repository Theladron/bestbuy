import store
import products
import user_input


def show_current_stock(shop):
    print()
    print(shop.get_total_quantity())
    print("----------")


def show_products(shop):
    print("----------")
    product_list = shop.get_all_products()
    for index in range(len(product_list)):
        print(f"{index+1}. {product_list[index].show()}")
    print("----------")


def make_order(shop):
    show_products(shop)
    product_list = shop.get_all_products()
    print("When you want to finish order, enter empty text.")
    order_list = []
    while True:
        item = user_input.order_item_input(product_list)
        quantity = user_input.order_quantity_input()
        if isinstance(item and quantity, int):
            order_list.append((product_list[item-1], quantity))
        else:
            break
    if order_list:
        print(shop.order(order_list))



def start(shop):
    menu_funct = {1: show_products,
                  2: show_current_stock,
                  3: make_order,
                  }
    while True:

        print("""
    Store Menu
    ----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit""")
        menu_choice = user_input.main_menu_input()
        if menu_choice == 4:
            exit()
        else:
            menu_funct[menu_choice](shop)


def main():

    product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()

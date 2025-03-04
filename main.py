import store
import products
import user_input


def show_current_stock(shop):
    """
    Gets total quantity of all products in the shop
    :param shop: Store class, loaded with products from Product class
    """
    print()
    print(shop.get_total_quantity())
    print("----------")


def show_products(shop):
    """
    Gets all products currently in the shop
    :param shop: Store class, loaded with products from Product class
    """
    print("----------")
    product_list = shop.get_all_products()
    for index in range(len(product_list)):
        print(f"{index+1}. {product_list[index].show()}")
    print("----------")


def make_order(shop):
    """
    Creates a list of tuples with product and quantity from repeated user inputs,
    calls the order from the list
    :param shop: Store class, loaded with products from Product class
    """
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
    """
    Shows the menu functions, gets user input and calls the functions
    interacting with the shop
    :param shop: Store class, loaded with products from Product class
    """
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
    """Created a list of product objects and starts the menu interface, handles exceptions"""
    try:
        product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250)
                        ]
        best_buy = store.Store(product_list)
    except ValueError as e:
        print(f"Error with the input values: {e}")
    except TypeError as e:
        print(f"Error with the input type: {e}")
    except NameError as e:
        print(f"Error catching name: {e}")
    else:
        start(best_buy)


if __name__ == "__main__":
    main()

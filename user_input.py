def main_menu_input():
    while True:
        try:
            menu_input = int(input("Please choose a number: "))
        except ValueError:
            print("Error. Please enter a number between 1-4.")
        else:
            if 1 <= menu_input <= 4:
                return menu_input
            else:
                print("Error. Please enter a number between 1-4.")


def order_item_input(product_list):
    while True:
        item_input = input("Which product # do you want? ")
        if not item_input:
            return item_input
        elif (item_input.isnumeric()
            and 1 <= int(item_input) <= len(product_list)):
            return int(item_input)
        else:
            print("Error. Please enter a valid product number or leave the input blank.")


def order_quantity_input():
    while True:
        menu_input = input("What amount do you want? ")
        if not menu_input:
            return menu_input
        elif menu_input.isnumeric():
            return int(menu_input)
        else:
            print("Error. Please enter a number or leave the input blank.")

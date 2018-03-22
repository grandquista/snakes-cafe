"""Snakes Cafe ordering menu."""
import math

from csv import DictReader
from locale import LC_ALL, currency, setlocale
from uuid import uuid4

from default.menu import (
    CATEGORY_VIEW, INSTRUCTIONS_HEADER, MENU, MENU_ERROR, ORDER_RECEIPT,
    ORDER_RECEIPT_LINE_ITEM, ORDER_RESPONSE, SALES_TAX, USER_INPUT_REQUEST,
    create_catgory_view)

setlocale(LC_ALL, '')


REQUEST_MENU_FILE = '''
Would you like to provide a file for loading a menu?
> '''


def category_display(category):
    """
    Display a single category with possible menu items.

    See sample output below

    Category
    --------
    Food1
    Food2
    """
    print(category.title())
    print('-' * len(category))
    for food in CATEGORY_VIEW[category]:
        print(food.title())


def menu_display():
    """
    Provide a menu for users.
    """
    print(INSTRUCTIONS_HEADER)
    for category in sorted(CATEGORY_VIEW.keys()):
        print()
        category_display(category)


def format_food_quantity(food, quantity):
    """
    Format beginning of receipt line item.
    """
    return '{} x{}'.format(food, quantity)


def receipt_display(order):
    """
    Format an order into a receipt.
    """
    sub_total = sub_total_cost(order)
    print(ORDER_RECEIPT.format(
        id=order['id'],
        total_due=format(currency(total_cost(order)), '>33'),
        subtotal=format(currency(sub_total), '>34'),
        sales_tax=format(currency(calculate_sales_tax(sub_total)), '>33'),
        items='\n'.join(
            ORDER_RECEIPT_LINE_ITEM.format(
                food=format_food_quantity(food, quantity),
                cost=format(
                    currency(cost_of_items(food, quantity)),
                    '>{}'.format(
                        42 - len(format_food_quantity(food, quantity)))))
            for food, quantity in order.items()
            if food != 'id'
        )
    ))


def remove_order_item(order, *food):
    """
    Remove food from order if contained.

    Inform the user if the item had not been added to their order.
    """
    food = ' '.join(food)
    if food not in order:
        print('{} not in order'.format(food))
    else:
        order[food] -= 1
        print('cost of order so far in {}'.format(currency(total_cost(order))))
        if order[food] == 0:
            order.pop(food)


def add_order_item(order, *food):
    """
    Add a food item to an order or inform user that it is not available.
    """
    try:
        quantity = int(food[-1])
        food = ' '.join(food[:-1])
    except(ValueError):
        quantity = 1
        food = ' '.join(food)
    if food not in MENU:
        print(MENU_ERROR.format(food))
        return

    if quantity <= 0:
        print('That is not a valid quantity!')
        return
    check_quantity = order.get(food, 0) + quantity

    if MENU[food]['quantity'] < check_quantity:
        print('That is too many! Not enough in stock.')
        return

    order[food] = check_quantity
    print(ORDER_RESPONSE.format(order[food], food))
    print('cost of order so far in {}'.format(currency(total_cost(order))))


def handle_user_action(order, user_request):
    """
    Dispatch to handler functions based on user action verb.
    """
    action, *options = user_request.split()
    if action == 'order':
        receipt_display(order)
    elif action == 'menu':
        menu_display()
    elif action == 'remove':
        remove_order_item(order, *options)
    elif action in CATEGORY_VIEW:
        category_display(user_request)
    else:
        add_order_item(order, action, *options)


def handle_input(order, user_request):
    """
    Handle input.

    false for exit, true otherwise
    """
    user_request = user_request.strip().lower()
    if not user_request:
        return True
    elif user_request == 'quit':
        return False
    handle_user_action(order, user_request)
    return True


def cost_of_items(food, quantity):
    """
    Retrieve the current price for a menu item and quantity.
    """
    return MENU[food]['price'] * quantity


def sub_total_cost(order):
    """
    Gather costs of idividual line items into a subtotal.
    """
    cost = 0
    for food, quantity in order.items():
        if food == 'id':
            continue
        cost += cost_of_items(food, quantity)
    return cost


def calculate_sales_tax(cost):
    """
    Calculate additional cost from sales tax.
    """
    return math.ceil(cost * SALES_TAX) / 100


def total_cost(order):
    """
    Calculate cost of order with sales tax added.
    """
    sub_total = sub_total_cost(order)
    sales_tax = calculate_sales_tax(sub_total)
    return sub_total + sales_tax


def generate_blank_order_with_id():
    """
    Create a new order with needed metadata.
    """
    return {'id': uuid4()}


def load_menu():
    global CATEGORY_VIEW, MENU
    file_name = clean_input(REQUEST_MENU_FILE)
    if not file_name:
        return
    try:
        with open(file_name) as istream:
            csv_content = istream.read()
    except OSError:
        print('File {} could not be found'.format(file_name))
        return
    menu = {}
    for row in DictReader(csv_content.splitlines(), fieldnames=[
            'name', 'categories', 'price', 'quantity']):
        try:
            price = float(row['price'].strip())
        except ValueError:
            print('found ({}) invalid number price'.format(row['price']))
            return
        if row['quantity'] is None:
            quantity = 1
        else:
            try:
                quantity = int(row['quantity'].strip())
            except ValueError:
                print('found ({}) invalid integer quantity'.format(
                    row['quantity']))
                return
        menu[row['name'].strip()] = {
            'categories': row['categories'].strip(),
            'price': price,
            'quantity': quantity,
        }
    MENU = menu
    CATEGORY_VIEW = create_catgory_view(MENU)


def clean_input(*args):
    """
    Handle standard input exceptions and get input line.
    """
    try:
        return input(*args)
    except EOFError:
        return 'quit'


def main():
    """main."""
    load_menu()
    menu_display()
    order = generate_blank_order_with_id()
    while handle_input(order, user_request=clean_input(USER_INPUT_REQUEST)):
        pass


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('quit should be used to exit cleanly')

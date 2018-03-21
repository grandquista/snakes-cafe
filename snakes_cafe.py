"""Snakes Cafe ordering menu."""

import math

from locale import LC_ALL, currency, setlocale
from uuid import uuid4

setlocale(LC_ALL, '')

INSTRUCTIONS_HEADER = '''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
'''

USER_INPUT_REQUEST = '''
***********************************
** What would you like to order? **
***********************************
> '''

ORDER_RECEIPT = '''
*******************************************
The Snakes Cafe
"Eatability Counts"

Order #{id}
===========================================
{items}
-------------------------------------------
Subtotal                         {subtotal}
Sales Tax                       {sales_tax}
---------
Total Due                       {total_due}
*******************************************
'''

ORDER_RECEIPT_LINE_ITEM = '{food} x{quantity} {cost}'

MENU_ERROR = '''
***********************************
** {} is not in menu **
***********************************
'''

ORDER_RESPONSE = '''
** {} order of {} have been added to your meal **
'''

MENU = {
    'wings': {
        'categories': 'appetizers',
        'price': 7.77
    },
    'cookies': {
        'categories': 'appetizers',
        'price': 100.0
    },
    'spring rolls': {
        'categories': 'appetizers',
        'price': 4.0
    },
    'fries': {
        'categories': 'appetizers',
        'price': 1.50
    },
    'calimari': {
        'categories': 'appetizers',
        'price': 3.45
    },
    'gyoza': {
        'categories': 'appetizers',
        'price': 6.78
    },
    'salmon': {
        'categories': 'entrees',
        'price': 16.0
    },
    'steak': {
        'categories': 'entrees',
        'price': 20.0
    },
    'meat tornado': {
        'categories': 'entrees',
        'price': 12.01
    },
    'spaghetti': {
        'categories': 'entrees',
        'price': 12.34
    },
    'tofu': {
        'categories': 'entrees',
        'price': 8.0
    },
    'stir fry': {
        'categories': 'entrees',
        'price': 10
    },
    'ice cream': {
        'categories': 'desserts',
        'price': 5.00
    },
    'cake': {
        'categories': 'desserts',
        'price': 3.99
    },
    'whole pie': {
        'categories': 'desserts',
        'price': 30.0
    },
    'tiramisu': {
        'categories': 'desserts',
        'price': 5.01
    },
    'mixed fruit': {
        'categories': 'desserts',
        'price': 0.0
    },
    'half a cookie': {
        'categories': 'desserts',
        'price': 0.50
    },
    'coffee': {
        'categories': 'drinks',
        'price': 0.85
    },
    'tea': {
        'categories': 'drinks',
        'price': 0.60
    },
    'blood of the innocent': {
        'categories': 'drinks',
        'price': 666.66
    },
    'orange juice': {
        'categories': 'drinks',
        'price': 2
    },
    'smoothie': {
        'categories': 'drinks',
        'price': 3.5
    },
    'ice cream float': {
        'categories': 'drinks',
        'price': 3.25
    },
    'coleslaw': {
        'categories': 'sides',
        'price': 1.00
    },
    '5 cheese sticks': {
        'categories': 'sides',
        'price': 2.00
    },
    'garlic bread': {
        'categories': 'sides',
        'price': 2.22
    },
    'chips with avocado dip': {
        'categories': 'sides',
        'price': 1.32
    },
    'salad': {
        'categories': 'sides',
        'price': 0.75
    },
    'fondue': {
        'categories': 'sides',
        'price': 4.80
    },
}

CATEGORY_VIEW = {}
for food, details in MENU.items():
    categories = details['categories']
    CATEGORY_VIEW.setdefault(categories, []).append(food)

SALES_TAX = 10.1


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
    print(INSTRUCTIONS_HEADER)
    for category in sorted(CATEGORY_VIEW.keys()):
        print()
        category_display(category)


def receipt_display(order):
    sub_total = sub_total_cost(order)
    print(ORDER_RECEIPT.format(
        id=order['id'],
        total_due=currency(total_cost(order)),
        subtotal=currency(sub_total),
        sales_tax=currency(calculate_sales_tax(sub_total)),
        items='\n'.join(
            ORDER_RECEIPT_LINE_ITEM.format(
                food=food,
                quantity=quantity,
                cost=currency(cost_of_items(food, quantity))
            )
            for food, quantity in order.items()
            if food != 'id'
        )
    ))


def remove_order_item(order, *food):
    food = ' '.join(food)
    if food not in order:
        print('{} not in order'.format(food))
    else:
        order[food] -= 1


def add_order_item(order, *food):
    food = ' '.join(food)
    if food not in MENU:
        print(MENU_ERROR.format(food))
        return
    order[food] = order.get(food, 0) + 1
    print(ORDER_RESPONSE.format(order[food], food))
    print('cost of order so far in {}'.format(currency(total_cost(order))))


def handle_user_action(order, user_request):
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
    function handles input
    false for exit, true otherwise
    """
    user_request = user_request.strip().lower()
    if user_request == 'quit':
        return False
    handle_user_action(order, user_request)
    return True


def cost_of_items(food, quantity):
    return MENU[food]['price'] * quantity


def sub_total_cost(order):
    cost = 0
    for food, quantity in order.items():
        if food == 'id':
            continue
        cost += cost_of_items(food, quantity)
    return cost


def calculate_sales_tax(cost):
    return math.ceil(cost * SALES_TAX) / 100


def total_cost(order):
    sub_total = sub_total_cost(order)
    sales_tax = calculate_sales_tax(sub_total)
    return sub_total + sales_tax


def generate_blank_order_with_id():
    return {'id': uuid4()}


def clean_input(*args):
    try:
        return input(*args)
    except EOFError:
        return 'quit'


def main():
    """main."""
    menu_display()
    order = generate_blank_order_with_id()
    while handle_input(order, user_request=clean_input(USER_INPUT_REQUEST)):
        pass


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('quit should be used to exit cleanly')

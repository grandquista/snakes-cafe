"""Snakes Cafe ordering menu."""

from typing import Dict

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


def menu_display():
    print(INSTRUCTIONS_HEADER)
    print('Appetizers')
    print('----------')
    for item, properties in MENU.items():
        if properties['categories'] == 'appetizers':
            print(item.title())
    print('\nEntrees')
    print('-------')
    for item, properties in MENU.items():
        if properties['categories'] == 'entrees':
            print(item.title())
    print('\nDesserts')
    print('--------')
    for item, properties in MENU.items():
        if properties['categories'] == 'desserts':
            print(item.title())
    print('\nDrinks')
    print('------')        
    for item, properties in MENU.items():
        if properties['categories'] == 'drinks':
            print(item.title())




def handle_input(order, user_request):
    """
    function handles input
    false for exit, true otherwise
    """
    user_request = user_request.strip().lower()
    if user_request == 'quit':
            return False
    if user_request not in MENU:
            print(MENU_ERROR.format(user_request))
    else:
            order[user_request] = order.get(user_request, 0) + 1
            print(ORDER_RESPONSE.format(order[user_request], user_request))
    return True


def main() -> None:
    """main."""
    menu_display()
    order = {}
    while handle_input(order, user_request=input(USER_INPUT_REQUEST)):
        pass

        
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('quit should be used to exit cleanly')

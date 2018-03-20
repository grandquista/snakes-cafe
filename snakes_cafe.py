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
        'categories': 'appetizers'
    },
    'cookies': {
        'categories': 'appetizers'
    },
    'spring rolls': {
        'categories': 'appetizers'
    },
    'salmon': {
        'categories': 'entrees'
    },
    'steak': {
        'categories': 'entrees'
    },
    'meat tornado': {
        'categories': 'entrees'
    },
    'ice cream': {
        'categories': 'desserts'
    },
    'cake': {
        'categories': 'desserts'
    },
    'pie': {
        'categories': 'desserts'
    },
    'coffee': {
        'categories': 'drinks'
    },
    'tea': {
        'categories': 'drinks'
    },
    'blood of the innocent': {
        'categories': 'drinks'
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

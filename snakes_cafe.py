"""Snakes Cafe ordering menu."""

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


def main() -> None:
    """main."""
    print(INSTRUCTIONS_HEADER)
    while True:
        user_request = input(USER_INPUT_REQUEST)
        if user_request == 'quit':
            break


if __name__ == '__main__':
    main()

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
Subtotal {subtotal}
Sales Tax {sales_tax}
---------
Total Due {total_due}
*******************************************
'''

ORDER_RECEIPT_LINE_ITEM = '{food} {cost}'

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

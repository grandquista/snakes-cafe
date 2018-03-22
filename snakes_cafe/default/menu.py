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
        'price': 7.77,
        'quantity': 10,
    },
    'cookies': {
        'categories': 'appetizers',
        'price': 100.0,
        'quantity': 10,
    },
    'spring rolls': {
        'categories': 'appetizers',
        'price': 4.0,
        'quantity': 10,
    },
    'pickled vegtables': {
        'categories': 'appetizers',
        'price': 7.77,
        'quantity': 10,
    },
    'butter rolls': {
        'categories': 'appetizers',
        'price': 100.0,
        'quantity': 10,
    },
    'hummus': {
        'categories': 'appetizers',
        'price': 4.0,
        'quantity': 10,
    },
    'fries': {
        'categories': 'appetizers',
        'price': 1.50,
        'quantity': 10,
    },
    'calimari': {
        'categories': 'appetizers',
        'price': 3.45,
        'quantity': 10,
    },
    'gyoza': {
        'categories': 'appetizers',
        'price': 6.78,
        'quantity': 10,
    },
    'salmon': {
        'categories': 'entrees',
        'price': 16.0,
        'quantity': 10,
    },
    'steak': {
        'categories': 'entrees',
        'price': 20.0,
        'quantity': 10,
    },
    'meat tornado': {
        'categories': 'entrees',
        'price': 12.01,
        'quantity': 10,
    },
    'chili': {
        'categories': 'entrees',
        'price': 16.0,
        'quantity': 10,
    },
    'mac and cheese': {
        'categories': 'entrees',
        'price': 20.0,
        'quantity': 10,
    },
    'jambalaya': {
        'categories': 'entrees',
        'price': 12.01,
        'quantity': 10,
    },
    'spaghetti': {
        'categories': 'entrees',
        'price': 12.34,
        'quantity': 10,
    },
    'tofu': {
        'categories': 'entrees',
        'price': 8.0,
        'quantity': 10,
    },
    'stir fry': {
        'categories': 'entrees',
        'price': 10,
        'quantity': 10,
    },
    'ice cream': {
        'categories': 'desserts',
        'price': 5.00,
        'quantity': 10,
    },
    'cake': {
        'categories': 'desserts',
        'price': 3.99,
        'quantity': 10,
    },
    'whole pie': {
        'categories': 'desserts',
        'price': 30.0,
        'quantity': 10,
    },
    'baklava': {
        'categories': 'desserts',
        'price': 5.00,
        'quantity': 10,
    },
    'biscotti': {
        'categories': 'desserts',
        'price': 3.99,
        'quantity': 10,
    },
    'rice pudding': {
        'categories': 'desserts',
        'price': 30.0,
        'quantity': 10,
    },
    'tiramisu': {
        'categories': 'desserts',
        'price': 5.01,
        'quantity': 10,
    },
    'mixed fruit': {
        'categories': 'desserts',
        'price': 0.0,
        'quantity': 10,
    },
    'half a cookie': {
        'categories': 'desserts',
        'price': 0.50,
        'quantity': 10,
    },
    'coffee': {
        'categories': 'drinks',
        'price': 0.85,
        'quantity': 10,
    },
    'tea': {
        'categories': 'drinks',
        'price': 0.60,
        'quantity': 10,
    },
    'blood of the innocent': {
        'categories': 'drinks',
        'price': 666.66,
        'quantity': 10,
    },
    'soda': {
        'categories': 'drinks',
        'price': 0.85,
        'quantity': 10,
    },
    'wine': {
        'categories': 'drinks',
        'price': 0.60,
        'quantity': 10,
    },
    'spring water': {
        'categories': 'drinks',
        'price': 666.66,
        'quantity': 10,
    },
    'orange juice': {
        'categories': 'drinks',
        'price': 2,
        'quantity': 10,
    },
    'smoothie': {
        'categories': 'drinks',
        'price': 3.5,
        'quantity': 10,
    },
    'ice cream float': {
        'categories': 'drinks',
        'price': 3.25,
        'quantity': 10,
    },
    'coleslaw': {
        'categories': 'sides',
        'price': 1.00,
        'quantity': 10,
    },
    '5 cheese sticks': {
        'categories': 'sides',
        'price': 2.00,
        'quantity': 10,
    },
    'garlic bread': {
        'categories': 'sides',
        'price': 2.22,
        'quantity': 10,
    },
    'potato chips': {
        'categories': 'sides',
        'price': 1.00,
        'quantity': 10,
    },
    'apple slices': {
        'categories': 'sides',
        'price': 2.00,
        'quantity': 10,
    },
    'mixed nuts': {
        'categories': 'sides',
        'price': 2.22,
        'quantity': 10,
    },
    'chips with avocado dip': {
        'categories': 'sides',
        'price': 1.32,
        'quantity': 10,
    },
    'salad': {
        'categories': 'sides',
        'price': 0.75,
        'quantity': 10,
    },
    'fondue': {
        'categories': 'sides',
        'price': 4.80,
        'quantity': 10,
    },
}

SALES_TAX = 10.1


def create_catgory_view(menu):
    category_view = {}
    for food, details in menu.items():
        categories = details['categories']
        category_view.setdefault(categories, []).append(food)
    return category_view


CATEGORY_VIEW = create_catgory_view(MENU)

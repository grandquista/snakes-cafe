"""Snakes Cafe ordering menu."""

import math

from csv import DictReader
from io import StringIO
from locale import LC_ALL, currency, setlocale
from sys import stdout
from uuid import uuid4

from default.menu import (
    CATEGORY_VIEW, INSTRUCTIONS_HEADER, MENU, ORDER_RECEIPT_HEAD,
    ORDER_RECEIPT_TAIL, REQUEST_MENU_FILE, SALES_TAX,
    USER_INPUT_REQUEST, create_catgory_view)

setlocale(LC_ALL, '')


class SnakesCafeError(Exception):
    """
    Base exception for library errors.
    """


class Order:
    def __init__(self):
        """
        Create a new order with needed metadata.
        """
        self.id = uuid4()
        self._order = {}

    def __repr__(self):
        """
        Represent an order in the following form.

        '<Order #{id} | Items: {item_count} | Total: {order_cost}>'.
        """
        return f'''<Order #{
            self.id
        } | Items: {
            len(self)
        } | Total: '{
            currency(self.total_cost())
        }'>'''

    def __str__(self):
        """
        Format an order into a receipt for printing.
        """
        with StringIO as ostream:
            self.display_order(ostream)
            return ostream.getvalue()

    def __getitem__(self, key):
        return self._order[key]

    def __setitem__(self, key, value):
        self._order[key] = value

    def __len__(self):
        return len(self._order)

    def __bool__(self):
        return bool(self._order)

    def __iter__(self):
        return iter(self._order.items())

    def __contains__(self, key):
        return key in self._order

    @staticmethod
    def category_display(category, ostream=stdout):
        """
        Display a single category with possible menu items.

        See sample output below

        Category
        --------
        Food1
        Food2
        """
        print(category.title(), file=ostream)
        print('-' * len(category), file=ostream)
        for food in CATEGORY_VIEW[category]:
            print(food.title(), file=ostream)

    def menu_display(self, ostream=stdout):
        """
        Provide a menu for users.
        """
        print(INSTRUCTIONS_HEADER, file=ostream)
        for category in sorted(CATEGORY_VIEW.keys()):
            print(file=ostream)
            self.category_display(category, ostream)

    def print_receipt(self):
        """
        Format an order into a receipt file.
        """
        with open(f'order-{ self.id }.txt') as ostream:
            self.display_order(ostream)

    def display_order(self, ostream=stdout):
        """
        Format an order and output to stream or stdout.
        """
        sub_total = self.sub_total_cost()
        print(ORDER_RECEIPT_HEAD.format(id=self.id), file=ostream)
        for food, quantity in self:
            print(
                format(food, '<23'),
                'x',
                format(quantity, '<5'),
                format(currency(self.cost_of_items(food, quantity)), '>11'),
                file=ostream)
        print(ORDER_RECEIPT_TAIL.format(
            total_due=format(currency(self.total_cost()), '>33'),
            subtotal=format(currency(sub_total), '>34'),
            sales_tax=format(
                currency(self.calculate_sales_tax(sub_total)), '>33'),
        ), file=ostream)

    def remove_item(self, food, quantity=1):
        """
        Remove food from order if contained.

        Inform the user if the item had not been added to their order.
        """
        if food not in self:
            return (food, 'not in order')
        self[food] -= quantity
        if self[food] <= 0:
            self._order.pop(food)
        return ('cost of order is', currency(self.total_cost()))

    def add_item(self, food, quantity=1):
        """
        Add a food item to an order or inform user that it is not available.
        """
        if food not in MENU:
            return (food, 'is not in menu')
        check_quantity = self._order.get(food, 0) + quantity

        if MENU[food]['quantity'] < check_quantity:
            return (check_quantity, 'is too many! Not enough in stock.')

        self[food] = check_quantity
        return (
            self[food],
            'order of',
            food,
            'have been added to your meal\ncost of order is',
            currency(self.total_cost()))

    @staticmethod
    def _handle_action_with_quantity(method, action):
        if not action:
            return ()
        try:
            quantity = int(action[-1])
            if quantity <= 0:
                return (action[-1], 'is not a valid quantity!')
        except ValueError:
            return method(' '.join(action))
        return method(' '.join(action[:-1]), quantity)

    def handle_user_action(self, user_request):
        """
        Dispatch to handler functions based on user action verb.
        """
        action = user_request.split()
        if action[0] == 'order':
            return self.display_order
        if action[0] == 'menu':
            return self.menu_display
        if action[0] == 'remove':
            return self._handle_action_with_quantity(
                self.remove_item, action[1:])
        if action[0] in CATEGORY_VIEW:
            return lambda *args: self.category_display(' '.join(action), *args)
        return self._handle_action_with_quantity(self.add_item, action)

    def handle_input(self, user_request, ostream=stdout):
        """
        Handle input.

        false for exit, true otherwise
        """
        user_request = user_request.strip().lower()
        if not user_request:
            return False
        elif user_request == 'quit':
            return True
        response = self.handle_user_action(user_request)
        if callable(response):
            response(ostream)
        else:
            print(*response, file=ostream)
        return False

    @staticmethod
    def cost_of_items(food, quantity):
        """
        Retrieve the current price for a menu item and quantity.
        """
        return MENU[food]['price'] * quantity

    def sub_total_cost(self):
        """
        Gather costs of idividual line items into a subtotal.
        """
        cost = 0
        for food, quantity in self:
            cost += self.cost_of_items(food, quantity)
        return cost

    @staticmethod
    def calculate_sales_tax(cost):
        """
        Calculate additional cost from sales tax.
        """
        return math.ceil(cost * SALES_TAX) / 100

    def total_cost(self):
        """
        Calculate cost of order with sales tax added.
        """
        sub_total = self.sub_total_cost()
        sales_tax = self.calculate_sales_tax(sub_total)
        return sub_total + sales_tax

    def load_menu(self, ostream=stdout):
        global CATEGORY_VIEW, MENU
        file_name = self.clean_input(REQUEST_MENU_FILE)
        if not file_name:
            return
        try:
            with open(file_name) as istream:
                csv_content = istream.read()
        except OSError:
            return print('File', file_name, 'could not be found', file=ostream)
        menu = {}
        for row in DictReader(csv_content.splitlines(), fieldnames=[
                'name', 'categories', 'price', 'quantity']):
            try:
                price = float(row['price'].strip())
            except ValueError:
                return print(
                    'found (', row, ') with invalid price', file=ostream)
            if row['quantity'] is None:
                quantity = 1
            else:
                try:
                    quantity = int(row['quantity'].strip())
                except ValueError:
                    return print(
                        'found (', row, ') with invalid quantity',
                        file=ostream)
            menu[row['name'].strip()] = {
                'categories': row['categories'].strip(),
                'price': price,
                'quantity': quantity,
            }
        MENU = menu
        CATEGORY_VIEW = create_catgory_view(MENU)

    @staticmethod
    def clean_input(*args):
        """
        Handle standard input exceptions and get input line.
        """
        try:
            return input(*args)
        except EOFError:
            return 'quit'

    def process_user_order(self, ostream=stdout):
        self.load_menu(ostream)
        self.menu_display(ostream)
        while not self.handle_input(
                self.clean_input(USER_INPUT_REQUEST),
                ostream):
            pass


def main():
    """main."""
    Order().process_user_order()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('quit should be used to exit cleanly')

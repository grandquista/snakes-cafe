"""Snakes Cafe ordering menu."""

import math

from csv import DictReader
from locale import LC_ALL, currency, setlocale
from sys import stdout
from uuid import uuid4

from default.menu import (
    CATEGORY_VIEW, INSTRUCTIONS_HEADER, MENU, MENU_ERROR, ORDER_RECEIPT,
    ORDER_RECEIPT_LINE_ITEM, ORDER_RESPONSE, REQUEST_MENU_FILE, SALES_TAX,
    USER_INPUT_REQUEST, create_catgory_view)

setlocale(LC_ALL, '')


class Order:
    def __init__(self):
        """
        Create a new order with needed metadata.
        """
        self.id = uuid4()
        self._order = {}

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

    def menu_display(self):
        """
        Provide a menu for users.
        """
        print(INSTRUCTIONS_HEADER)
        for category in sorted(CATEGORY_VIEW.keys()):
            print()
            self.category_display(category)

    @staticmethod
    def format_food_quantity(food, quantity):
        """
        Format beginning of receipt line item.
        """
        return '{} x{}'.format(food, quantity)

    def print_receipt(self):
        """
        Format an order into a receipt.
        """
        with open(f'order-{ self.id }.txt') as ostream:
            self.display_order(ostream)

    def display_order(self, ostream=stdout):
        """
        Format beginning of receipt line item.
        """
        sub_total = self.sub_total_cost()
        print(ORDER_RECEIPT.format(
            id=self.id,
            total_due=format(currency(self.total_cost()), '>33'),
            subtotal=format(currency(sub_total), '>34'),
            sales_tax=format(
                currency(self.calculate_sales_tax(sub_total)), '>33'),
            items='\n'.join(
                ORDER_RECEIPT_LINE_ITEM.format(
                    food=self.format_food_quantity(food, quantity),
                    cost=format(
                        currency(self.cost_of_items(food, quantity)),
                        '>{}'.format(42 - len(
                            self.format_food_quantity(food, quantity)))))
                for food, quantity in self
            )
        ), file=ostream)

    def remove_item(self, food):
        """
        Remove food from order if contained.

        Inform the user if the item had not been added to their order.
        """
        if food not in self:
            print('{} not in order'.format(food))
        else:
            self[food] -= 1
            print('cost of order so far in {}'.format(
                currency(self.total_cost())))
            if self[food] == 0:
                self._order.pop(food)

    def add_item(self, food, quantity=1):
        """
        Add a food item to an order or inform user that it is not available.
        """
        if quantity <= 0:
            print('That is not a valid quantity!')
            return
        if food not in MENU:
            print(MENU_ERROR.format(food))
            return
        check_quantity = self._order.get(food, 0) + quantity

        if MENU[food]['quantity'] < check_quantity:
            print('That is too many! Not enough in stock.')
            return

        self[food] = check_quantity
        print(ORDER_RESPONSE.format(self[food], food))
        print('cost of order so far in {}'.format(currency(self.total_cost())))

    def handle_user_action(self, user_request):
        """
        Dispatch to handler functions based on user action verb.
        """
        action = user_request.split()
        if action[0] == 'order':
            self.display_order()
        elif action[0] == 'menu':
            self.menu_display()
        elif action[0] == 'remove':
            self.remove_item(' '.join(action[1:]))
        elif action[0] in CATEGORY_VIEW:
            self.category_display(user_request)
        else:
            try:
                quantity = int(action[-1])
            except ValueError:
                self.add_item(' '.join(action))
            else:
                self.add_item(' '.join(action[:-1]), quantity)

    def handle_input(self, user_request):
        """
        Handle input.

        false for exit, true otherwise
        """
        user_request = user_request.strip().lower()
        if not user_request:
            return True
        elif user_request == 'quit':
            return False
        self.handle_user_action(user_request)
        return True

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

    def load_menu(self):
        global CATEGORY_VIEW, MENU
        file_name = self.clean_input(REQUEST_MENU_FILE)
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

    @staticmethod
    def clean_input(*args):
        """
        Handle standard input exceptions and get input line.
        """
        try:
            return input(*args)
        except EOFError:
            return 'quit'

    def process_user_order(self):
        self.load_menu()
        self.menu_display()
        while self.handle_input(
                user_request=self.clean_input(USER_INPUT_REQUEST)):
            pass


def main():
    """main."""
    Order().process_user_order()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('quit should be used to exit cleanly')

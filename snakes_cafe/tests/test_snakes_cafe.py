from snakes_cafe import snakescafe as sc


# handles true
def test_handle_input_valid_menu_order_returns_true():
    """
    should return true
    """
    assert sc.handle_input({}, 'whole pie')


# handles false
def test_handle_input_quit_returns_false():
    assert not sc.handle_input({}, 'quit')


def test_handle_input_not_case_sensitive():
    order = {}
    assert sc.handle_input(order, 'WhOlE PiE')
    assert 'whole pie' in order


def test_handle_input_takes_item_and_quantity():
    order = {}
    assert sc.handle_input(order, 'whole pie 5')
    assert 'whole pie' in order
    assert order['whole pie'] == 5


def test_sub_total_cost_returns_zero_for_empty_order():
    assert sc.sub_total_cost({}) == 0


def test_sub_total_cost_returns_non_zero_when_ordering_whole_pie():
    assert sc.sub_total_cost({'whole pie': 1}) != 0


def test_calculate_sales_tax_is_10_1_percent():
    assert sc.calculate_sales_tax(100) == 10.10
    assert sc.calculate_sales_tax(1.00) == 0.11


def test_generate_blank_order_with_id():
    first_order = sc.generate_blank_order_with_id()
    assert first_order
    second_order = sc.generate_blank_order_with_id()
    assert second_order
    assert first_order['id'] != second_order['id']


def test_format_food_quantity_3():
    assert sc.format_food_quantity('food', 3) == 'food x3'


def test_format_food_quantity_1():
    assert sc.format_food_quantity('food', 1) == 'food x1'


def test_remove_order_item_in_order():
    order = {'wings': 6}
    sc.remove_order_item(order, 'wings')
    assert order['wings'] == 5


def test_remove_order_item_not_in_order():
    order = {'food': 6}
    sc.remove_order_item(order, 'tofu')
    assert order['food'] == 6


def test_remove_order_item_erases_entry():
    order = {'wings': 2}
    sc.remove_order_item(order, 'wings')
    sc.remove_order_item(order, 'wings')
    assert 'wings' not in order


def test_add_order_item_in_menu():
    order = {}
    sc.add_order_item(order, 'tofu')
    assert order['tofu'] == 1


def test_add_order_item_not_in_menu():
    order = {}
    sc.add_order_item(order, 'food')
    assert not order


def test_handle_user_action_remove_item():
    order = {'salad': 3}
    sc.handle_user_action(order, 'remove salad')
    assert order['salad'] == 2


def test_handle_user_action_add_item():
    order = {'salad': 3}
    sc.handle_user_action(order, 'salad')
    assert order['salad'] == 4


def test_handle_user_action_display_order():
    order = sc.generate_blank_order_with_id()
    sc.add_order_item(order, 'salad')
    sc.add_order_item(order, 'salad')
    sc.add_order_item(order, 'salad')
    sc.handle_user_action(order, 'order')
    assert order['salad'] == 3


def test_cost_of_items_2_salad():
    assert sc.cost_of_items('salad', 2) == 1.5


def test_cost_of_items_2_tofu():
    assert sc.cost_of_items('tofu', 2) == 16.0


def test_sub_total_cost_3_salad():
    assert sc.sub_total_cost({'salad': 3}) == 2.25


def test_sub_total_cost_empty_order():
    assert sc.sub_total_cost(sc.generate_blank_order_with_id()) == 0


def test_sub_total_cost_3_tofu():
    assert sc.sub_total_cost({'tofu': 3}) == 24.0


def test_total_cost_3_salad():
    assert sc.total_cost({'salad': 3}) == 2.48


def test_total_cost_empty_order():
    assert sc.total_cost(sc.generate_blank_order_with_id()) == 0


def test_total_cost_3_tofu():
    assert sc.total_cost({'tofu': 3}) == 26.43


def test_add_order_item_quantity_cannot_be_negative():
    order_variable = sc.generate_blank_order_with_id()
    sc.add_order_item(order_variable, 'tea', -1)
    assert 'tea' not in order_variable


def test_add_order_item_quantity_can_be_positive():
    order_variable = sc.generate_blank_order_with_id()
    sc.add_order_item(order_variable, 'tea', 1)
    assert 'tea' in order_variable


def test_add_order_item_quantity_cannot_exceed_stock():
    order_variable = sc.generate_blank_order_with_id()
    sc.add_order_item(order_variable, 'tea', 12)
    assert 'tea' not in order_variable

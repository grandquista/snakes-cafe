import snakes_cafe as sc


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
    order = {'food': 6}
    sc.remove_order_item(order, 'food')
    assert order['food'] == 5


def test_remove_order_item_not_in_order():
    order = {'food': 6}
    sc.remove_order_item(order, 'tofu')
    assert order['food'] == 6


def test_add_order_item_in_menu():
    order = {}
    sc.add_order_item(order, 'tofu')
    assert order['tofu'] == 1


def test_add_order_item_not_in_menu():
    order = {}
    sc.add_order_item(order, 'food')
    assert not order

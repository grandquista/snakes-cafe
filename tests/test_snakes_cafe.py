import snakes_cafe as sc

import pytest


@pytest.fixture
def order():
    return sc.Order()


def test_handle_input_valid_menu_order_returns_true(order):
    assert not order.handle_input('whole pie')


def test_handle_input_quit_returns_false(order):
    assert order.handle_input('quit')


def test_handle_input_not_case_sensitive(order):
    assert not order.handle_input('WhOlE PiE')
    assert 'whole pie' in order


def test_handle_input_takes_item_and_quantity(order):
    assert not order.handle_input('whole pie 5')
    assert 'whole pie' in order
    assert order['whole pie'] == 5


def test_sub_total_cost_returns_zero_for_empty_order(order):
    assert order.sub_total_cost() == 0


def test_sub_total_cost_returns_non_zero_when_ordering_whole_pie(order):
    order.add_item('tofu')
    assert order.sub_total_cost() != 0


def test_calculate_sales_tax_is_10_1_percent(order):
    assert order.calculate_sales_tax(100) == 10.10
    assert order.calculate_sales_tax(1.00) == 0.11


def test_generate_blank_order_with_id(order):
    assert order.id
    second_order = sc.Order()
    assert second_order.id
    assert order.id != second_order.id


def test_format_food_quantity_3(order):
    assert order.format_food_quantity('hummus', 3) == 'hummus x3'


def test_format_food_quantity_1(order):
    assert order.format_food_quantity('hummus', 1) == 'hummus x1'


def test_remove_item_in_order(order):
    order.add_item('hummus', 6)
    order.remove_item('hummus')
    assert order['hummus'] == 5


def test_remove_item_not_in_order(order):
    order.add_item('hummus', 6)
    order.remove_item('tofu')
    assert order['hummus'] == 6


def test_remove_item_erases_entry(order):
    order.add_item('hummus', 2)
    order.remove_item('hummus')
    order.remove_item('hummus')
    assert 'hummus' not in order


def test_add_item_in_menu(order):
    order.add_item('tofu')
    assert order['tofu'] == 1


def test_add_item_not_in_menu(order):
    order.add_item('food')
    assert not order


def test_handle_user_action_remove_item(order):
    order.add_item('salad', 3)
    order.handle_user_action('remove salad')
    assert order['salad'] == 2


def test_handle_user_action_add_item(order):
    order.add_item('salad', 3)
    order.handle_user_action('salad')
    assert order['salad'] == 4


def test_handle_user_action_display_order(order):
    order.add_item('salad')
    order.add_item('salad')
    order.add_item('salad')
    order.handle_user_action('order')
    assert order['salad'] == 3


def test_cost_of_items_2_salad(order):
    assert order.cost_of_items('salad', 2) == 1.5


def test_cost_of_items_2_tofu(order):
    assert order.cost_of_items('tofu', 2) == 16.0


def test_sub_total_cost_3_salad(order):
    order.add_item('salad', 3)
    assert order.sub_total_cost() == 2.25


def test_sub_total_cost_empty_order(order):
    assert order.sub_total_cost() == 0


def test_sub_total_cost_3_tofu(order):
    order.add_item('tofu', 3)
    assert order.sub_total_cost() == 24.0


def test_total_cost_3_salad(order):
    order.add_item('salad', 3)
    assert order.total_cost() == 2.48


def test_total_cost_empty_order(order):
    assert order.total_cost() == 0


def test_total_cost_3_tofu(order):
    order.add_item('tofu', 3)
    assert order.total_cost() == 26.43


def test_add_item_quantity_cannot_be_negative(order):
    order.handle_user_action('tea -1')
    assert 'tea' not in order


def test_add_item_quantity_can_be_positive(order):
    order.add_item('tea', 1)
    assert 'tea' in order


def test_add_item_quantity_cannot_exceed_stock(order):
    order.add_item('tea', 12)
    assert 'tea' not in order

<!-- List out in words each test that you intend to write
For each test that you intend to write, name the function or functions that you intend to call and test
If you change your tests, update your test plan -->

# Test Plan

## Existing functions

#### test_handle_input
  - check that it returns false when the user enters quit
  - check that otherwise it returns true on a valid command
  - check that user input is not case sensitive

#### test_calculate_sales_tax
  - test that it correctly calculates 10.1 % sales tax from the total before tax (subtotal)

#### test_generate_blank_order_with_id
  - test that a unique id is generated for each order

#### test_format_food_quantity
  - test for expected string formatting of food receipt line

#### test_remove_order_item
  - test that it removes the corresponding item when the user types remove the name of the item, and that it then triggers the order to display
  - test that it does nothing when item is not in order

#### test_add_order_item
  - item on the menu is added to the order total
  - item not on the menu is ignored

#### test_handle_user_action
  - test that `remove` user command functions
  - test that `add` user command functions
  - test that `order` user command functions

#### test_cost_of_items
  - test cost with 2 salads
  - test cost with default empty order
  - test cost with 2 tofu

#### test_sub_total_cost
  - test that it returns 0 when the order is empty
  - test sub total cost with 3 salads
  - test sub total cost with 3 tofu

#### test_total_cost
  - test that it returns 0 when the order is empty
  - test cost with 3 salads
  - test cost with 3 tofu

## Planned Functions

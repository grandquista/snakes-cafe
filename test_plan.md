<!-- List out in words each test that you intend to write
For each test that you intend to write, name the function or functions that you intend to call and test
If you change your tests, update your test plan -->

# Test Plan

## Existing functions

#### handle_input
check that it prompts user for input
check that it returns false when the user enters quit
check that otherwise it returns true
check that user input is not case sensitive

#### menu_display
Test menu display by examining if the menu prints, and has all desired items and categories

#### main
NO TEST
takes user input


## Planned Day 2 Functions

#### total_cost
test that it takes an order and returns the total cost with tax

#### display_order
test that when the user types order all the items in their order are displayed, with total cost

#### generate_blank_order_with_id
test that a new order is added to the queue

#### calculate_sales_tax
test that it correctly calculate sales tax from the total before tax (subtotal)

#### print_menu
test that it displays the menu only when the user types menu

#### present_categories
test that it displays the categories and their items to the user when the user types the corresponding category name

#### remove_item
test that it removes the corresponding item when the user types remove the name of the item, and that it then triggers the order to display


# Snakes Cafe

**Author**: Patricia Raftery, Adam Grandquist
**Version**: 1.0.0

## Overview
This is a cafe menu that prompts the user for an order. It then acknowledges the user's order by printing what they ordered, and the amount.

## Getting Started
To build this app, create a dictionary that contains the menu of the cafe. Write code that displays the menu to user. Display an intro, and prompt the user for their order. Acknowledge the user's order by displaying the ordered item, and the amount. If the item is not on the menu, tell the user it is not on the menu.
This application uses 2 packages, pytest and uuid. These should be setup in a virtual environment before running this application.

## Architecture
This application is written using Python3, and Markdown for the README. It uses uuid for a unique order ID. The locale module is used for currency handling.

## API
No API is used for this project.

## Change Log

#### Day 1
03-19-2018 6:00pm - Displays the menu to the user.

03-19-2018 5:20pm - Wrote app functionality. Wrote menu dictionary, wrote code to accept user input, displays menu choice back to user, quits when user types quit.

03-19-2018 4:33pm - Created project framework.

#### Day 2
03-20-2018 9:00pm - uuid imported to provide unique order ID, user input dispatches on commands.

03-20-2018 8:00pm - Fixed test for tax calculation and truncation.

03-20-2018 5:00pm - 6 tests written, code passes 5/6 tests.

03-20-2018 4:00pm - Prices added to each item. Subtotal and sales tax functions started.

03-20-2018 3:00pm - Added sides category, and made each category have 6 items.

03-20-2018 2:00pm - Created new files, like test_plan.md and test_snakes_cafe.py

#### Day 3
03-21-2018 3:42pm - Update test plan based on new work.

03-21-2018 3:20pm -
  - Fix exception on empty user input.
  - Add tests for order cost calculations
  - Add tests for user input handling functions.

03-21-2018 3:00pm -
  - Add tests for adding and removing items from order.
  - Right justify all order formatting, and order formatting.

03-21-2018 2:30pm - Implement remove items from order and refactored adding items.

03-21-2018 10:00am - Updating README and test plan based on new reading.

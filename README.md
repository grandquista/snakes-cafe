# Snakes Cafe

**Author**: Patricia Raftery, Adam Grandquist
**Version**: 1.0.0

## Overview
This is a cafe menu that prompts the user for an order. It then acknowledges the user's order by printing what they ordered, and the amount.

## Getting Started
To build this app, create a dictionary that contains the menu of the cafe. Write code that displays the menu to user. Display an intro, and prompt the user for their order. Acknowledge the user's order by displaying the ordered item, and the amount. If the item is not on the menu, tell the user it is not on the menu.
This application uses 2 packages, pytest and uuid. These should be setup in a virtual environment before running this application.

## Architecture
This application is written using Python3, and Markdown for the README. It uses uuid for a unique order ID.

## API
No API is used for this project.

## Change Log

#### Day 1
03-19-2018 6:00pm - Displays the menu to the user.

03-19-2018 5:20pm - Wrote app functionality. Wrote menu dictionary, wrote code to accept user input, displays menu choice back to user, quits when user types quit.

03-19-2018 4:33pm - Created project framework.

#### Day 2
03-19-2018 5:00pm - 6 tests written, code passes 5/6 tests.

03-19-2018 4:00pm - Prices added to each item. Subtotal and sales tax functions started, uuid imported for unique order ID.

03-19-2018 3:00pm - Added sides category, and made each category have 6 items.

03-19-2018 2:00pm - Created new files, like test_plan.md and test_snakes_cafe.py
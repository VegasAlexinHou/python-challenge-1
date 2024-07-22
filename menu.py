#Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}
# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order=[]
# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order?")

    # Create a variable for the menu item number
    i = 1

    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")

        # Store the menu category associated with its menu item number
        menu_items[i] = key

        # Add 1 to the menu item number
        i += 1
    print(menu_items)
    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]

            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1

            # 2. Ask customer to input menu item number
            menu_selection = input("What would you like from the menu? ")
            # Check if the customer input is a valid number
            if menu_selection.isdigit():
                menu_selection = int(menu_selection)
                # Check if the menu selection item number is in the menu_items dictionary
                if menu_selection in menu_items.keys():
                    # Retrieve the menu selection details
                    menu_selection_item = menu_items[menu_selection]
                    print(f"You selected: {menu_selection_item['Item name']} - $ {menu_selection_item['Price']}")
                    # 3. Ask the customer for the quantity of the menu item
                    quantity = input("How many would you like to order? ")
                    # Check if the quantity is a number, default to 1 if not
                    if quantity.isdigit():
                        quantity = int(quantity)
                    else:
                        quantity = 1
                    # 4. Add the item name, price, and quantity to the order list
                    order.append({
                        "Item name": menu_selection_item["Item name"],
                        "Price": menu_selection_item["Price"],
                        "Quantity": quantity
                    })
                else:
                    print("Invalid item number. Please select a valid item number.")
            else:
                print("Invalid input. Please enter a valid item number.")
        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    while True:
        # 5. Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ").strip().lower()
        if keep_ordering == 'y':
            break
        elif keep_ordering == 'n':
            place_order = False
            break
        else:
            print("Invalid input. Please enter 'Y' for yes or 'N' for no.")

# 7. Print out the customer's order
print("This is what we are preparing for you.\n")

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 8. Loop through the items in the customer's order
total_cost = 0
for item in order:
    # 9. Store the dictionary items as variables
    item_name = item["Item name"]
    item_price = item["Price"]
    item_quantity = item["Quantity"]

    # 10. Calculate the number of spaces for formatted printing
    num_item_spaces = 24 - len(item_name)
    num_price_spaces = 6 - len(f"{item_price:.2f}")
    num_quantity_spaces = 10 - len(str(item_quantity))

    # 11. Create space strings
    item_spaces = " " * num_item_spaces
    price_spaces = " " * num_price_spaces
    quantity_spaces = " " * num_quantity_spaces

    # 12. Print the item name, price, and quantity
    print(f"{item_name}{item_spaces} | ${item_price:.2f}{price_spaces} | {item_quantity}{quantity_spaces}")

    # 13. Calculate the cost of the order using list comprehension
    total_cost += item_price * item_quantity

# Print the total cost
print(f"\nTotal cost: ${total_cost:.2f}")


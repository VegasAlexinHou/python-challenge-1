# python-challenge-1

Order System
1. Create an empty list. This list will later store a customer's order in dictionary format, as follows:

[
  {
    "Item name": "string",
    "Price": float,
    "Quantity": int
  },
  {
    "Item name": "string",
    "Price": float,
    "Quantity": int
  },
]

        
        #We will create a list here for the customers selections and it will create it in a dictionary format.
        
        order = []
        being that order = [] will store the informarion for the "Item name" : "string, "Price" : Float, etc.

2. After the sub-menu is printed, prompt the customer to enter their selection from the menu, saving it as a variable menu_selection.
        
        #Using the input we will create the prompts for the customer and it will make it a variable 
        
        menu_selection = input("What would you like from the menu?")
        
        NOTE: I worked with tutor Brandon Wong here. I had #2 broken out, but kept getting errors. He walked me through some things and was very helpful but after I followed his direction, thess commands became simplified.
        

3. Use input validation to check if the customer input menu_selection is a number. If it isn't, print an error message. If it is a number, convert the input to an integer and use it to check if it is in the keys of menu_items.

        #We are working here to turn the input into a number.  I worked with the AI assitant here and then kept testing it with the Tutor. 

4. If the user input is not in the menu_items keys, print an error. Otherwise, perform the following actions:

Get the item name from the menu_items dictionary and store it as a variable.

Ask the customer for the quantity of the menu item, using the item name variable in the question, and let them know that the quantity will default to 1 if their input is invalid. Save their answer as a variable called quantity.

Check that the customer input is a number. If it isn't, set the quantity to the value 1. If it is a number, convert the variable to an integer.

Append the customer's order to the order list in dictionary format with the following keys: "Item name", "Price", and "Quantity. You will need this information to print the receipt at the end of the order. The price should be found in the menu_items dictionary.

    #We are setting up how the input is taken in and how the program will act based on the decisions. We will see i fthe menu_selection is a valid key in menu_ites, retrieve this information and print it, ask the user for quantity of their selection, add to the order with .append command. I used the AI assitant to set this up. I created a blank .py and worked with the formula and then tried to get it into my file. My tutor helped as much here as we had time. 

5. Inside the continuous while loop that prompts the customer if they would like to keep ordering, write a match:case statement that checks for y or n (upper or lowercase), and includes a default option if neither letter is entered by the customer. The following actions should be performed for each case:

y: Set the place_order variable to True and break from the continuous while loop.

n: Set the place_order variable to False, print "Thank you for your order", and break from the continuous while loop.

Default: Tell the customer to try again because they didn't type a valid input.

    #We are finding out if the customer wants to keep ordering. The input will be translated accordingly to end the order process. The 'n' command will identify as flase and break the ordering chain. If type something other than 'y' or 'n', it will give them an invalid response to start the order again.
    
      while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ").strip().lower()
        if keep_ordering == 'y':
            break
        elif keep_ordering == 'n':
            place_order = False
            break
        else:
            print("Invalid input. Please enter 'Y' for yes or 'N' for no.")
    

Order Receipt

6. Create a for loop to loop through the order list.
        
        #We will go through the items ordered and we will designate the items from the dictionary in the order list. 
        
       from tutor:   for item in order: 
                        item name, item price, item quantity (for # 7 )


7. Inside the loop, save the value of each key as their own variable: item_name, price, and quantity.

       for item in order: 
                        item name, item price, item quantity (for # 7 )


8. Calculate the number of empty spaces that should be added to the display so that the receipt uses the following format:

Item name                 | Price  | Quantity
--------------------------|--------|----------
Apple                     | $0.49  | 1
Tea - Thai iced           | $3.99  | 2
Fried banana              | $4.49  | 3

num_items_spaces = 24 - len(item_name)
num_prices_spaces = 6 -
len(f"[item_price:.2f}")
num_quantity_spaces = 10 -
len(str(item_quantity)

****Not advised this did match up to the code****
table.add_row

9. Create the space strings as their own variables using string multiplication.

item_spaces = " " * num_item_spaces
price_spaces = " " * num_prices_spaces
quantitity_spaces = " " *
num_quantity_spaces

10. Print the line for the receipt using the format in Step 8.
       
        print(f"{item_name}{item_spaces} | ${item_price:.2f}{price_spaces} | {item_quantity}{quantity_spaces}")
        
        
11. Upon exiting the for loop, use list comprehension and sum() to calculate the total price of the order and display it to the customer. Make sure you multiply the price by the quantity in your list comprehension.
   
    Uses a loop to calculate the total cost by summing up the price times the quantity for each item in the order, Print total cost at the end.


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Print how many resources the coffee machine has left
# Check if resources are sufficient
# Process coins
# Check if transaction is successful
# Make coffee

def main():
    # Machine starts with $0
    money = 0

    # Loop infinitely since project has no defined exit condition
    while True:
        user_input = input("What would you like? (espresso/latte/cappuccino): ")

        # Print current resources and money stored if user types 'report'
        if user_input == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${money}")
            pass
        # Calculate cost of resources for type of drink entered
        else:
            drink_cost = MENU[user_input]["cost"]
            drink_water = MENU[user_input]["ingredients"]["water"]
            drink_coffee = MENU[user_input]["ingredients"]["coffee"]
            if user_input != "espresso":
                drink_milk = MENU[user_input]["ingredients"]["milk"]
            else:
                drink_milk = 0
            
            # Calculate resources remaining
            water_left = resources['water'] - drink_water
            coffee_left = resources['coffee'] - drink_coffee
            milk_left = resources['milk'] - drink_milk     

            # Checks for sufficient water
            if water_left < 0:
                print("Sorry there is not enough water.")
                pass
            # Checks for sufficient coffee
            elif coffee_left < 0:
                print("Sorry there is not enough coffee.")
                pass
            # Checks for sufficient milk
            elif milk_left < 0: 
                print("Sorry there is not enough milk.")
                pass
            else:
                # Ask user to input quantity of each type of coin
                print("Please insert coins.")
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickels = int(input("How many nickels? "))
                pennies = int(input("How many pennies? "))

                # Calculate amount entered based on coins
                amount_entered = (quarters*25+dimes*10+nickels*5+pennies)/100

                # Calculate change to give back to user
                change = amount_entered - MENU[user_input]["cost"]

                # Checks if user input enough coins
                if change < 0:
                    print("Sorry that's not enough money. Money refunded.")
                    pass
                # If sufficient coins entered and resources, deplete used resources and add money to machine
                else:
                    resources['water'] = water_left
                    resources['coffee'] = coffee_left
                    resources['milk'] = milk_left
                    money += drink_cost
                    print(f"Here is ${change:.2f} in change.")
                    print(f"Here is your {user_input} ☕️. Enjoy!")
        

if __name__ == "__main__":
    main()
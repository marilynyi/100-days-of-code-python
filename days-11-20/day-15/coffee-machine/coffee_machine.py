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

# Loop while coffee machine is on
# If user wants to print a report
#   Print current resources and profit
# Else if user wants to turn machine off
#   Turn machine off
# Else display drink types and prompt user to select
#   Ask user to select a drink
#   If machine has sufficient resources
#       Ask user to input coins
#           If user inputs at least total amount
#               Give back change
#               Give drink
#           Else
#               Refund money
#               Restart loop
#   Else display 'insufficient resource' message and restart loop

# Machine starts with $0
profit = 0
    
def main():

    is_on = True

    # Loop while coffee machine is on
    while is_on:

        # Ask user for a drink type
        print("Coffee Machine Menu")
        print(f'1. Espresso: ${MENU["espresso"]["cost"]:.2f}')
        print(f'2. Latte: ${MENU["latte"]["cost"]:.2f}')
        print(f'3. Cappuccino: ${MENU["cappuccino"]["cost"]:.2f}')
        user_input = input("What would you like? (espresso/latte/cappuccino): ")

        # Print current resources and money stored if user types 'report'
        if user_input == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${profit}")
            pass
        # Turn off coffee machine if user types 'off'
        elif user_input == "off":
            return False
        # Give user drink after valid drink type and payment inputs if machine has sufficient resources
        else:
            drink = MENU[user_input]
            if sufficient_resources(drink["ingredients"]):
                payment = calculate_payment()
                if sufficient_payment(payment, drink["cost"]):
                    give_drink(drink["ingredients"], user_input)


def sufficient_resources(drink_ingredients):
    """Check if machine has sufficient resources to make drink"""
    for ingredient in drink_ingredients:
        if resources[ingredient] < drink_ingredients[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def calculate_payment():
    """Calculate coins entered as dollars and change value"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))

    # Calculate amount entered based on coins
    payment = (quarters*25+dimes*10+nickels*5+pennies)/100

    return payment


def sufficient_payment(payment, drink_cost):
    """Check if payment is sufficient"""
    # Calculate change to give back to user
    if payment < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        global profit
        change = payment - drink_cost
        profit += drink_cost
        print(f"Here is ${change:.2f} in change.")
        return True       


def give_drink(drink_ingredients, drink):
    """Deplete used resources from machine to make drink"""
    for ingredient in drink_ingredients:
        resources[ingredient] -= drink_ingredients[ingredient]
    
    print(f"Here is your {drink} ☕️. Enjoy!")


if __name__ == "__main__":
    main()
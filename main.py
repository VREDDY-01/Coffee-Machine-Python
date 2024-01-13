from data import MENU, resources

RES_MENU = MENU
RES_resources = resources
ifOn = True


def check_resources(user_input):
    if RES_MENU[user_input]["ingredients"]["water"] > RES_resources["water"]:
        return False
    elif RES_MENU[user_input]["ingredients"]["coffee"] > RES_resources["coffee"]:
        return False
    elif user_input != "espresso" and RES_MENU[user_input]["ingredients"]["milk"] > RES_resources["milk"]:
        return False
    else:
        return True


while ifOn:
    userInput = input("What would you like? (espresso/latte/cappuccino):").lower()
    if userInput == "off":
        ifOn = False
        continue
    if userInput == "report":
        print(f"water: {RES_resources["water"]}ml")
        print(f"milk: {RES_resources["milk"]}ml")
        print(f"coffee: {RES_resources["coffee"]}g")
        continue
    is_available = check_resources(userInput)
    if is_available:
        print("Please insert the coins >")
        quarters = float(input("Insert no of quarters:"))
        dimes = float(input("Insert no of dimes:"))
        pennies = float(input("Insert no of pennies:"))
        nickels = float(input("Insert no of nickels:"))
        total = (quarters*0.25)+(dimes*0.10)+(nickels*0.5)+(pennies*0.01)
        change = total - RES_MENU[userInput]["cost"]
        if change < 0:
            print("Sorry that's Not Enough. Money Refunded.")
            continue
        else:
            RES_resources["water"] = RES_resources["water"] - RES_MENU[userInput]["ingredients"]["water"]
            RES_resources["coffee"] = RES_resources["coffee"] - RES_MENU[userInput]["ingredients"]["coffee"]
            if userInput != "espresso":
                RES_resources["milk"] = RES_resources["milk"] - RES_MENU[userInput]["ingredients"]["milk"]
            print(f"Here is ${round(change, 2)} dollars in change.")
            print(f"Here is your {userInput} ☕. Enjoy!")
    else:
        print("Sorry there is not enough resources.")
        continue

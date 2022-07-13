from data import MENU, resources

# TODO 1
# dictionary selector for type of drink
# resource management
continue_state = True

while continue_state:

    def coin_to_cost_conversion(quarters, dimes, nickles, pennies):
        """converts coin amount into total paid"""
        total = quarters * .25 + dimes * .10 + nickles * .05 + pennies * .01
        return total


    def sufficient_payment(payment, charge):
        """calculates if payment is sufficient for charge"""
        if payment < charge:
            return False
        else:
            return True


    def return_amount(payment, cost_of_drink):
        """Takes in payment and cost, calculates refund """
        return payment - cost_of_drink


    def resource_deduction(drink):
        """Takes out the resource for drink"""
        for ingredient in drink["ingredients"]:
            resources[ingredient] -= drink['ingredients'][ingredient]
            print(f"coffee resources: {resources[ingredient]} vs drink cost: {drink['ingredients'][ingredient]}")


    def enough_ingredients(drink):
        for ingredient in drink["ingredients"]:
            if (drink["ingredients"][ingredient]) > resources[ingredient]:
                print(f"Sorry not enough {ingredient}")
                return False
            else:
                return True


    drink_selection = input("what would you like? (espresso/latte/cappuccino) ").lower()

    if drink_selection == "off":
        continue_state = False
        break
    if drink_selection == "print":
        for key in resources:
            print(f"{key.capitalize()}: {resources[key]}")
    else:
        cost = MENU[drink_selection]["cost"]
        print(f'That will cost: ${MENU[drink_selection]["cost"]}')

        if not enough_ingredients(MENU[drink_selection]):
            continue_state = False
        else:
            print("Please insert coins.")
            quarters_inserted = int(input("how many quarters? "))
            dimes_inserted = int(input("how many dimes? "))
            nickles_inserted = int(input("how many nickles? "))
            pennies_inserted = int(input('how many pennies? '))

            total_paid = coin_to_cost_conversion(quarters_inserted, dimes_inserted, nickles_inserted, pennies_inserted)
            remainder = total_paid - cost
            print(f"total paid: ${total_paid}, total due: ${cost}, remainder: ${total_paid - cost}")

            # TODO 2
            # calculate if payment is enough

            if sufficient_payment(total_paid, cost):
                print(f"Here is your {drink_selection}")
                resources["money"] += cost
                resource_deduction(MENU[drink_selection])
                if remainder > 0:
                    print(f"here is your change: {return_amount(total_paid, cost)}")
            else:
                print(f"insufficient funds for {drink_selection}")
                print(f"")

            # TODO 3
            # determine if enough resources and keep track of resources

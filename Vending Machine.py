class VendingMachine:

    def __init__(self):
        self.snacks = [
            ("01", "Oman Chips\U0001F35F", 1.0, 5),
            ("02", "Cheetos\U0001F35F", 3.5, 5),
            ("03", "Doritos\U0001F35F", 3.5, 4),
            ("04", "Sohar Chips\U0001F35F", 2.0, 3),
            ("05", "Salad Chips\U0001F35F", 1.5, 5),
        ]

        self.drinks = [
            ("01", "Laban Up\U0001F95B", 1.5, 5),
            ("02", "Water\U0001F4A7", 1.0, 5),
            ("03", "Mountain Dew\U0001F964", 3.0, 4),
            ("04", "Litchi\U0001F379", 2.5, 3),
            ("05", "Red Bull\U0001F964", 5.0, 5),
        ]

        self.chocolate = [
            ("01", "Kit Kat\U0001F36B", 3.5, 5),
            ("02", "Galaxy\U0001F36B", 4.0, 3),
            ("03", "Cadbury\U0001F36B", 3.0, 5),
            ("04", "Snickers\U0001F36B", 2.5, 4),
            ("05", "Bounty\U0001F36B", 2.5, 2),
        ]

        self.desserts = [
            ("01", "Cookies\U0001F36A", 6.5, 5),
            ("02", "Brownies\U0001F9C1", 8.0, 3),
            ("03", "Cupcakes\U0001F9C1", 10.0, 4),
            ("04", "Pudding Cups\U0001F36E", 15.5, 3),
            ("05", "Muffins\U0001F9C1", 9.0, 5),
        ]

        self.electronics = [
            ("01", "Speakers\U0001F508", 200.0, 5),
            ("02", "Headphones\U0001F3A7", 75.0, 4),
            ("03", "USB\U0001F4F1", 85.0, 5),
            ("04", "LED Flashlights\U0001F526", 20.0, 3),
            ("05", "Power Banks\U0001F50B", 150.0, 4),
        ]

        # Initialize a dictionary to keep track of the money in the machine
        self.money_in_machine = {
            'total': 0.0,
            'quarters': 10,
            'dimes': 10,
            'nickels': 10,
            'pennies': 10
        }

        self.dispensed_items = []

    def display_items(self, category):
        self.display_items_helper(category)

    def display_items_helper(self, item_type):
        for item in item_type:
            print("Item Id: {} --- Item Name: {}".format(item[0], item[1]))
            print("Item Price: {:.2f} DHS --- Stock: {}".format(item[2], item[3]))
        print()

    def main(self):
        while True:
            print("\033[1m🌟 Welcome to Alon's Vending Delight!🎊 Let the magic of our offerings enhance your day!🌟\033[0m")
            print("Select the category of item you want to buy:")
            print("1. Snacks\U0001F96B")
            print("2. Drinks\U0001F379")
            print("3. Chocolate\U0001F36B")
            print("4. Desserts\U0001F370")
            print("5. Electronics\U0001F4BB")
            print("6. Quit \u2716")

            choice = input("Enter your choice: ")

            if choice in ["1", "2", "3", "4", "5"]:
                category = self.get_category(int(choice))
                self.display_items(category)
                total_amount = self.purchase_item(category)
                if total_amount > 0:
                    self.accept_payment(total_amount)
            elif choice == "6":
                print("Thank you for using the vending machine!")
                break
            else:
                print("Invalid choice. Please try again.")

    def get_category(self, choice):
        categories = [self.snacks, self.drinks, self.chocolate, self.desserts, self.electronics]
        return categories[choice - 1]
    
    def purchase_item(self, item_type):
        total_amount = 0
        while True:
            item_id = input("Enter the Item Id you want to purchase (or 'cancel' to go back): ")
            if item_id.lower() == 'cancel':
                break

            for item in item_type:
                if item[0] == item_id:
                    if item[3] > 0:
                        quantity = int(input("Enter the quantity: "))
                        if quantity <= item[3] and quantity > 0:
                            total_amount += quantity * item[2]
                            print("Total amount: {:.2f}".format(total_amount))
                            break
                        else:
                            print("Invalid quantity. Please enter a valid quantity.")
                    else:
                        print("Sorry, this item is out of stock.")
                        break
            else:
                print("Invalid item id. Please try again.")
                continue  # Continue the loop if the item ID is invalid

        # Update stock after confirming the purchase
        for item in item_type:
            if item[0] == item_id:
                item[3] -= quantity
                break

        return total_amount

    def accept_payment(self, total_amount):
        print("Please pay the amount: {:.2f} DHS".format(total_amount))

        # Modify the prompts and conversion rates for DHS dirhams
        quarters = int(input("Enter the number of 1 DHS coins: "))
        dimes = int(input("Enter the number of 0.5 DHS coins: "))
        nickels = int(input("Enter the number of 0.25 DHS coins: "))
        pennies = int(input("Enter the number of 0.10 DHS coins: "))

        # Conversion rates for DHS dirhams
        dhs_quarter = 1.0
        dhs_dime = 0.5
        dhs_nickel = 0.25
        dhs_penny = 0.10

        # Calculate the total amount paid in DHS dirhams
        amount_paid = dhs_quarter * quarters + dhs_dime * dimes + dhs_nickel * nickels + dhs_penny * pennies

        if amount_paid < total_amount:
            print("Insufficient funds. Please insert more coins.")
        else:
            change = amount_paid - total_amount
            self.dispense_change(change)
            print("Thank you for your purchase!")
            print("Change: {:.2f} DHS".format(change))
            self.display_dispensed_items()  # Call the method to display dispensed items
            print("Please take your items.")

    def dispense_change(self, change):
        # Convert change to coins
        quarters = int(change // 0.25)
        change %= 0.25
        dimes = int(change // 0.1)
        change %= 0.1
        nickels = int(change // 0.05)
        change %= 0.05
        pennies = int(change // 0.01)

        # Update the money in the machine
        self.money_in_machine['quarters'] += quarters
        self.money_in_machine['dimes'] += dimes
        self.money_in_machine['nickels'] += nickels
        self.money_in_machine['pennies'] += pennies
        self.money_in_machine['total'] += (0.25 * quarters + 0.1 * dimes + 0.05 * nickels + 0.01 * pennies)

    def display_dispensed_items(self):
        if self.dispensed_items:
            print("Dispensing items:")
            for item in self.dispensed_items:
                print("Item Name: {} --- Quantity: {}".format(item[1], item[2]))
            print()
            # Clear the dispensed items list after displaying
            self.dispensed_items = []

if __name__ == "__main__":
    vending_machine = VendingMachine()
    vending_machine.main()

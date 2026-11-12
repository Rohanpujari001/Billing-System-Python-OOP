
# ==================================================
#          BILLING SYSTEM USING PYTHON OOP
# ==================================================

import math
import random
from datetime import datetime


# 1. PRODUCT CLASS
class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity


# 2. BILL CLASS
class Bill:

    GST_RATE = 0.18

    def __init__(self):
        self.products = []
        self.invoice_number = random.randint(1000, 9999)
        self.date = datetime.now().strftime("%d-%m-%Y %H:%M")

    def add_product(self, product):
        self.products.append(product)
        print("Product added successfully!")

    def remove_product(self, product_name):

        for product in self.products:

            if product.name.lower() == product_name.lower():
                self.products.remove(product)
                print("Product removed successfully!")
                return

        print("Product not found!")

    def calculate_subtotal(self):

        total = 0

        for product in self.products:
            total += product.calculate_total()

        return total

    # Polymorphism: Base discount method
    def calculate_discount(self):
        return 0

    def calculate_tax(self):

        taxable_amount = (
            self.calculate_subtotal() - self.calculate_discount()
        )

        return taxable_amount * self.GST_RATE

    def calculate_grand_total(self):

        total = (
            self.calculate_subtotal()
            - self.calculate_discount()
            + self.calculate_tax()
        )

        # Round payable amount up to the next whole rupee
        return math.ceil(total)

    def display_bill(self):

        if not self.products:
            print("\nNo products available in the cart!")
            return

        print("\n")
        print("=" * 65)
        print("                    SHOP BILL")
        print("=" * 65)

        print("Invoice Number:", self.invoice_number)
        print("Date:", self.date)

        print("-" * 65)

        print(
            "{:<20} {:<10} {:<12} {:<12}".format(
                "Product", "Price", "Quantity", "Total"
            )
        )

        print("-" * 65)

        for product in self.products:

            print(
                "{:<20} {:<10.2f} {:<12} {:<12.2f}".format(
                    product.name,
                    product.price,
                    product.quantity,
                    product.calculate_total()
                )
            )

        print("-" * 65)

        subtotal = self.calculate_subtotal()
        discount = self.calculate_discount()
        tax = self.calculate_tax()
        grand_total = self.calculate_grand_total()

        print("\nSubtotal       : Rs.", round(subtotal, 2))
        print("Discount       : Rs.", round(discount, 2))
        print("GST (18%)      : Rs.", round(tax, 2))
        print("-" * 40)
        print("Final Amount   : Rs.", grand_total)

        print("=" * 65)
        print("          THANK YOU FOR SHOPPING!")
        print("=" * 65)


# 3. PREMIUM BILL CLASS (INHERITANCE)
class PremiumBill(Bill):

    def calculate_discount(self):

        # Premium customers get 10% discount
        return self.calculate_subtotal() * 0.10


# 4. MAIN BILLING SYSTEM
def main():

    print("=" * 50)
    print("          WELCOME TO BILLING SYSTEM")
    print("=" * 50)

    bill = None

    # Select customer type
    while True:

        print("\nSelect Customer Type:")
        print("1. Normal Customer")
        print("2. Premium Customer")

        customer_choice = input("Enter choice (1-2): ")

        if customer_choice == "1":
            bill = Bill()
            print("\nNormal Customer Selected!")
            break

        elif customer_choice == "2":
            bill = PremiumBill()
            print("\nPremium Customer Selected!")
            break

        else:
            print("Invalid choice! Try again.")

    # Main Menu
    while True:

        print("\n========== BILLING MENU ==========")

        print("1. Add Product")
        print("2. Remove Product")
        print("3. View Cart")
        print("4. Generate Final Bill")
        print("5. Exit")

        choice = input("\nEnter Your Choice: ")

        try:

            if choice == "1":

                print("\n---------- ADD PRODUCT ----------")

                name = input("Enter Product Name: ").strip()

                if not name:
                    print("Product name cannot be empty!")
                    continue

                price = float(input("Enter Product Price: Rs. "))
                quantity = int(input("Enter Quantity: "))

                if price <= 0 or quantity <= 0:
                    print("Price and quantity must be positive!")
                    continue

                product = Product(name, price, quantity)

                bill.add_product(product)

                print("Product:", name)
                print("Total: Rs.", product.calculate_total())

            elif choice == "2":

                name = input("Enter Product Name to Remove: ")

                bill.remove_product(name)

            elif choice == "3":

                bill.display_bill()

            elif choice == "4":

                bill.display_bill()

                if bill.products:
                    break

            elif choice == "5":

                print("\nThank you for visiting!")
                break

            else:

                print("Invalid Choice! Please select 1-5.")

        except ValueError:

            print("Invalid Input! Please enter correct values.")

    print("\nProgram Closed Successfully!")


# 5. PROGRAM EXECUTION
if __name__ == "__main__":

    main()

# ==================================================
#                  END OF PROJECT
# ==================================================

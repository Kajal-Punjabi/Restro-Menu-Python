# Restaurant Menu Code

# Sample menu items with prices
menu = {
    "Burger": 120,
    "Pizza": 150,
    "Pasta": 180,
    "Salad": 100,
    "Soda": 90,
}

# Function to display the menu
def display_menu():
    print("\n--- Restaurant Menu ---")
    for item, price in menu.items():
        print(f"{item}: INR {price:.2f}")

# Function to take the order
def take_order():
    order = {}
    while True:
        item = input("Enter the item you want to order (or type 'done' to finish): ").title()
        if item.lower() == 'done':
            break
        elif item in menu:
            quantity = int(input(f"How many {item}s would you like to order? "))
            if item in order:
                order[item] += quantity
            else:
                order[item] = quantity
        else:
            print("Sorry, we don't have that item.")
    return order

# Function to calculate the bill
def calculate_bill(order):
    total = 0
    print("\n--- Your Order ---")
    for item, quantity in order.items():
        price = menu[item] * quantity
        total += price
        print(f"{item} x{quantity}: INR {price:.2f}")
    print(f"Total Bill: INR {total:.2f}")

# Main function to run the program
def main():
    while True:
        print("\nWelcome to the Restaurant!")
        print("1. View Menu")
        print("2. Place Order")
        print("3. Exit")
        choice = input("Please choose an option: ")

        if choice == '1':
            display_menu()
        elif choice == '2':
            order = take_order()
            calculate_bill(order)
        elif choice == '3':
            print("Thank you for visiting! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()

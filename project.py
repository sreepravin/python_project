import sys

# Global variables to store booking and customer details
bookings = []
drivers = []

# Customer Login Function
def customer_login():
    print("\n-- Customer Login --")
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username and password:
        print(f"\nLogin successful! Welcome, {username}.")
        customer_booking(username)
    else:
        print("Invalid login! Please try again.")
        customer_login()

# Customer Booking Function
def customer_booking(username):
    pickup = input("Enter Pickup Location: ")
    drop = input("Enter Drop Location: ")

    # Calculating a mock fare based on a flat rate per character difference (a simple simulation)
    distance = abs(len(pickup) - len(drop)) + 5  # Adding a base distance
    total_fare = distance * 10  # $10 per unit distance

    # Storing booking details
    booking = {
        'customer': username,
        'pickup': pickup,
        'drop': drop,
        'fare': total_fare
    }

    bookings.append(booking)

    print(f"\nBooking confirmed from {pickup} to {drop}.")
    print(f"Total fare: ${total_fare:.2f}")

    print("\n1. Logout")
    print("2. Exit")
    choice = input("Enter your choice: ")
    if choice == "2":
        sys.exit()

# Driver Login Function
def driver_login():
    print("\n-- Driver Login --")
    driver_name = input("Enter Driver Name: ")
    password = input("Enter Password: ")

    if driver_name and password:
        print(f"\nLogin successful! Welcome, {driver_name}.")
        show_customer_details(driver_name)
    else:
        print("Invalid login! Please try again.")
        driver_login()

# Function to Show Customer Details to the Driver
def show_customer_details(driver_name):
    if bookings:
        print("\n-- Available Bookings --")
        for booking in bookings:
            print(f"Customer: {booking['customer']}")
            print(f"Pickup Location: {booking['pickup']}")
            print(f"Drop Location: {booking['drop']}")
            print(f"Total Fare: ${booking['fare']:.2f}\n")
    else:
        print("No bookings available at the moment.")

    print("\n1. Logout")
    print("2. Exit")
    choice = input("Enter your choice: ")
    if choice == "2":
        sys.exit()

# Main Menu
def main():
    while True:
        print("\n--- Welcome to the Console Cab Booking System ---")
        print("1. Customer Login")
        print("2. Cab Driver Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            customer_login()
        elif choice == "2":
            driver_login()
        elif choice == "3":
            print("Thank you for using our service. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Starting the program
if __name__ == "__main__":
    main()

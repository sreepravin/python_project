class Cab:
    def __init__(self, cab_id, cab_type, availability=True):
        self.cab_id = cab_id
        self.cab_type = cab_type
        self.availability = availability

    def __str__(self):
        return f"Cab ID: {self.cab_id}, Type: {self.cab_type}, Available: {self.availability}"


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def __str__(self):
        return f"User ID: {self.user_id}, Name: {self.name}"


class CabBookingSystem:
    def __init__(self):
        self.cabs = []
        self.users = []

    def add_cab(self, cab):
        self.cabs.append(cab)

    def add_user(self, user):
        self.users.append(user)

    def book_cab(self, user_id):
        available_cabs = [cab for cab in self.cabs if cab.availability]
        if not available_cabs:
            print("No cabs available at the moment.")
            return

        print("Available cabs:")
        for cab in available_cabs:
            print(cab)

        cab_id = input("Enter the Cab ID to book: ")
        for cab in available_cabs:
            if cab.cab_id == cab_id:
                cab.availability = False
                print(f"Cab {cab.cab_id} booked successfully for User {user_id}.")
                return
        print("Invalid Cab ID.")

    def show_users(self):
        print("Registered Users:")
        for user in self.users:
            print(user)


def main():
    system = CabBookingSystem()

    # Add some cabs
    system.add_cab(Cab("C001", "Sedan"))
    system.add_cab(Cab("C002", "SUV"))
    system.add_cab(Cab("C003", "Minivan"))

    # Add some users
    system.add_user(User("U001", "Alice"))
    system.add_user(User("U002", "Bob"))

    while True:
        print("\nWelcome to the Cab Booking System")
        print("1. Book a Cab")
        print("2. Show Registered Users")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            user_id = input("Enter your User ID: ")
            system.book_cab(user_id)
        elif choice == "2":
            system.show_users()
        elif choice == "3":
            print("Thank you for using the Cab Booking System.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()

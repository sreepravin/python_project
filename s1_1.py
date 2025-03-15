import datetime
from datetime import timedelta
import sys
global bookings
bookings=[]
class customer_login:
    def login(self):
        print("\n ---Costomer Login ---")
        self.username=input("Enter your Username: ")
        self.password=input("Enter your password: ")
        if self.username and self.password:
            print(f"\n ***Login Successful***\n---Welcome {self.username}.")
            book=customer_booking()
            book.c_booking(self.username)
            
        else:
            print("Invalid login ,please try again.")
            c=customer_login()
            c.login()

class customer_booking:
    def c_booking(self,username):
        self.pickup=input("Enter pickup location :")
        self.drop=input("Enter drop location :")
        distance=(abs(len(self.pickup)-len(self.drop)))+5
        self.price=distance*10
        date1 = datetime.datetime.today().date()
        time1 = datetime.datetime.now().time()
        self.booking={
            'customer':username,
            'pickup':self.pickup,
            'drop':self.drop,
            'pickup_date':date1,
            'pickup_time':(datetime.datetime.combine(date1, time1) + timedelta(hours=1)).time(),
            'price':self.price
            }
        bookings.append(self.booking)
        print(f"Booking confirmed for {username}.")
        print(f"Pickup: {self.pickup}, \nDrop: {self.drop}, \nPrice: ${self.price}")

        print("\n1.Logout")
        print("\n2.Exit")
        choice=input("Enter your choice: ")
        if choice =="2":
            print("\n==================================================")
            sys.exit()
        
    def show_customer_details(self):
        if bookings:
            print("\n***Available Bookings***")
            for booking in bookings:
                print(f"Customer: {booking['customer']}")
                print(f"Pickup Location: {booking['pickup']}")
                print(f"Drop Location: {booking['drop']}")
                print(f"pickup data: {booking['pickup_date']}")
                print(f"pickup_time: {booking['pickup_time']}")
                print(f"Total Fare: ${booking['price']:.2f}\n")
        else:
            print("No booking available at moment.")
        print("\n1.Logout")
        print("\n2.Exit")
        choice =input("Enter your choice: ")
        if choice == "2":
            print("\n==================================================")

            sys.exit()
        
class driver_login_page:
    def driver_login(self):
        print("---Driver login---")
        self.driver_name=input("Enter drinver Name: ")
        self.password=input("Enter password : ")
        if self.driver_name and self.password:
            print(f"\n ***Login successful! welome {self.driver_name}")
            cb=customer_booking()
            cb.show_customer_details()
            
        else:
            print("Invalid login! please try again.")
            d=driver_login_page()
            d.driver_login()

    
        
if __name__ == "__main__":
    #def main():
    cus=customer_login()
    while True:
        print("\n==================================================")
        print("***WELCOME***")
        print("1.Customer Login")
        print("2.Cab Driver Login")
        print("3.Exit")
        choice = int(input("Enter yourn Choice: "))
        if choice==1:
            print("customer login page")
            cus.login()
        elif choice==2:
            print("cab driver login page")
            c=driver_login_page()
            c.driver_login()
        elif choice==3:
            print("******Thank you have a nice day******")
            print("\n==================================================")
            sys.exit()
        else:
            print("Invalid input")
            print("\n==================================================")











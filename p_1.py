import sys
from datetime import datetime
class customer_login:
    def login(self):
        print("\n ---Customer Login ---")
        self.username=input("Enter your Username: ")
        self.password=input("Enter your password: ")
        if self.username and self.password:
            print(f"\n ***Login Successful***!\n---Welcome {self.username}---.")
            book=customer_booking()
            book.booking(self.username) 
        else:
            print("Invalid login ,please try again.")
            self.login()
        print("1.logout")
        print("2.Exit")
        n1=int(input())
        if n1==2:
          sys.exit
class cab_driver_login:
    def login_1(self):
        print("\n --- cab Driver login --- ")
        self.username=input("Enter your username: ")
        self.password=input("Enter  your password: ")
        if self.username and self.password:
            print(f"\n**login successfull!**\n---Welcome{self.username}----.")
            customer_booking.show()
        else:
            print("Invalid login, please try again")
            self.login_1()
        print("1.logout")
        print("2.Exit")
        n2=int(input("Enter your choice:"))
        if n2==2:
            sys.exit()
class customer_booking:
   customer_details=[]
   def booking(self,username):
        pickup=input("Enter pickup location") #booking_date = current_time.strftime("%Y-%m-%d")  # Date in YYYY-MM-DD format
                                              #booking_time = current_time.strftime("%H:%M:%S")  # Time in HH:MM:SS format
        drop=input("Enter drop location")
        time=datetime.now()
        booking_time=time.strftime("%Y-%m-%d")
        booking_date=time.strftime("%H-%M-%S")
        distance=(abs(len(pickup)-len(drop)))+5
        price=distance*10
        #print("Total Amount RS: ",price)
        details={
        "username": username,
        "pickup": pickup,
        "drop": drop,
        "Amount":price,
        "booking_time":booking_time,
        "booking_date":booking_date
        }
        customer_booking.customer_details.append(details)
        print(f"Booking succesfully {username} Total Amount {price} ")


   @classmethod       
   def show(cls):
        if cls.customer_details:
            print("The customer details are:")
            for c in cls.customer_details:
               print(f" Customer :{c['username']}\n Pickup:{c['pickup']}\n Drop:{c['drop']}\n Price:{c['Amount']}\n Booking_date:{c['booking_date']}\n Booking_time{c['booking_time']}")
        else:
            print(" No customer have booked yet") 
def main():
        while True:
            print("\n==================================================")
            print("***WELCOME***")
            print("1.Customer Login")
            print("2.Cab Driver Login")
            print("3.Exit")
            choice = int(input("Enter yourn Choice: "))
            if choice==1:
                print("customer login page")
                cus=customer_login()
                cus.login()
            elif choice==2:
                print("cab driver login page")
                cab=cab_driver_login()
                cab.login_1()
            elif choice==3:
                print("Thank you have a nice day")
                print("\n==================================================")
                sys.exit()
                break
            else:
                print("Invalid input")
                print("\n==================================================")

if __name__ == "__main__":
    main()







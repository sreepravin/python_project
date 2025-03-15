
class customer_login:
    def login(self):
        print("\n ---Costomer Login ---")
        global self.username=input("Enter your Username: ")
        global self.password=input("Enter your paeewoed: ")
        if self.username and self.password:
            print(f"\n ***Login Successful***\n---Welcome {self.username}.")
            book=customer_booking()
            book.booking()
            
        else:
            print("Invalid login ,please try again.")
            c=customer_login()
            c.login()c

        
class customer_booking:
    def booking(self):
        global pickup=input("Enter pickup location : ")
        global drop=input("Enter drop location : ")
        global distance=(abs(len(pickup)-len(drop)))+5
        global price=distance*10
        print(price)

        
class customer_store:
    def customer_dis(self):
        global bookings[]
        global booking = {
            'customer'=self.username,
            'pickup'=pickup,
            'drop'= drop,
            'price'=price
            }
        bookings.append(booking)
        

class show_customer_details:
    def customer_show(self):
        if bookings:
            print("\n--Available Bookings--")
            for booking in bookings:
                print(f"Custrome name : {booking['customer']} ")
                print(f"Pickup Location : {booking['piclup']} ")
                print(f"Drop Location : {booking['drom']}")
                print(f"Total Fare : $(booking['price']}")
        else:
            print("no booking available at the movent")
                
        
        
        

class driver_login_page:
    def driver_login(self):
        print("---Driver login---")
        self.driver_name=input("Enter drinver Name: ")
        self.password=input("Enter password : ")
        if self.driver_name and self.password:
            print(f"\n ***Login successful! welome {self.driver_name}")
            
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
            d=driver_login_page()
            d.driver_login()
        elif choice==3:
            print("Thank you have a nice day")
            print("\n==================================================")
            break
        else:
            print("Invalid input")
            print("\n==================================================")











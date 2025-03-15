
class customer_login:
    def login(self):
        print("\n ---Costomer Login ---")
        self.username=input("Enter your Username: ")
        self.password=input("Enter your password: ")
        if self.username and self.password:
            print(f"\n ***Login Successful***\n---Welcome {self.username}.")
            
        else:
            print("Invalid login ,please try again.")
            c=customer_login()
            c.login()
class customer_booling:
    def booking(self):
        

        
        


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
        elif choice==3:
            print("Thank you have a nice day")
            print("\n==================================================")
            break
        else:
            print("Invalid input")
            print("\n==================================================")











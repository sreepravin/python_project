l=[]
l1=[]
l2=[]
class TaskManager:
    def add(self):
        n2=[]
        n1=int(input("Enter how many task to be added : "))
        for i in range(1,n1+1):
            print("Enter the task:",i)
            n2=input()
            n3="INCOMPLETE"
            l1.append(n2)
            l2.append(n3)
        l.append(l1)
        l.append(l2)
    def update(self):
        j=1
        for i in l1:
            print(j,".",i)
            j+=1
        n5=int(input("Enter How Many task to be updated : "))
        for i in  range(n5):
            n4=int(input("Enter the Task ID :"))
            n5=n4-1
            l2[n5]="COMPLETED"
        
    def live(self):
        for i in range(len(l1)):
            if(l2[i]=="INCOMPLETE"):
                print(l1[i])
    def com(self):
        for i in range(len(l1)):
            if(l2[i]=="COMPLETED"):
                print(l1[i])
def main():
    while(True):
        print("-------------------------------")
        print("1.Add Task ")
        print("2.Update Task")
        print("3.Display Live task")
        print("4.Display Completed Task")
        print("5.Exit")
        print("-------------------------------")
        n=int(input("Enter your choice:"))
        if(n==1):
            a=TaskManager() 
            a.add() 
        elif(n==2):
            b=TaskManager() 
            b.update()
        elif(n==3):
            c=TaskManager() 
            c.live()
        elif(n==4):
            d=TaskManager() 
            d.com()
        elif(n==5):
            print("Thank you!")
            print("-------------------------------")
            break
        else:
            print("Invalid input!!")  

main()        

#To connect python and sql to form management system for grocery store
import mysql.connector

mydb=mysql.connector.connect(
  host="localhost",
  user="root",
  password="filler21(03)"
)
mycursor=mydb.cursor()
mycursor.execute("Use grocery")
mydb.commit
def start():
    t=True
    while t==True:
        print("===================")
        print("WELCOME TO TERAMART")
        print("===================")
        x=input("Do you have an account with Teramart(yes/no):")
        x.lower()
        if x=="yes":
            d=int(input("Great, please enter your 13 digit account number:"))
            mycursor.execute("Select * from customer where accountno="+str(d))
            mydb.commit
            s=mycursor.fetchall()
            if s==[]:
                print("""Your account does not exist. Please either make an account 
                      or enter correct id""")
                continue
            main()
        elif x=="no":
            f=input("Would you like to make an account today, it is free of charge(yes/no):")
            f.lower
            if f=="yes":
                account()
            else:
                print("Ok,Thank you for your time")
                t=False
        else:
            print("Please enter proper response")
            continue
        

def account():
    x=input("Enter your name:")
    y=input("Enter year of birth:")
    c=input("Enter month of birth in number form(01 is january):")
    d=input("Enter the day of the month:")
    a=y+'-'+c+'-'+d
    print(a)
    phone= input("Enter your phone number:")
    mail= input("Enter your beginning of gmail address without @gmail.com part:")
    address= input("Enter your address:")
    values=(x,a,phone,mail,address)
    print(values)
    mycursor.execute("""Insert into customer name, dateofbirth, phonenumber, emailid, address
values (%s,%s,%s,%s,%s)""",values)
    mydb.commit
    mycursor.execute("Select accountno from customer where phonenumber="+phone)
    acc=mycursor.fetchall()
    print("Your account number is",str(acc))
    print("THANK YOU for making an account with us. We hope to see you again soon.")

def main():
    print("Enter 1 to make new groceries purchase from TeraMart")
    print("Enter 2 to check previous purchases from TeraMart")
    print("Enter 3 to alter customer infromation")
    print("Enter 4 to look at all the items present in store")
    choice=int(input())
    if choice==1:(
        mycursor.execute("Select * from grocerylist")
        mydb.commit()
        al= mycursor.fetchall()
        for i in al:
            print(i)
        num = 0
        itemlist={}
        h= int(input("Enter the number of unique items you are going to buy:")
        mycursor.execute("Select itemname from grocerylist")
        mydb.commit()
        items= mycursor.fetchall()
        while num<h:
              p=input("Enter item to buy")
              if p not in items:
                  print("Enter proper item name")
                  continue
              l=int(input("Enter number of items to buy"))
              num+=1
              itemlist[p]=l
        print("All the items you bought are:")
        print(itemlist)
        print("The total cost of this is:")
        cost=0)
        for key in itemlist:
              mycursor.execute("Select cost from grocerylist where itemname="+key)
              mydb.commit()
              val= mycursor.fetchall()
              cost+=val*itemlist[key]
        print(cost)

start()

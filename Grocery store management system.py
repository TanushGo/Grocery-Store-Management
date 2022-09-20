#To connect python and sql to form management system for grocery store
#Made By Tanush Goel

import mysql.connector

mydb=mysql.connector.connect(
  host="localhost",
  user="root",
  password="filler21(03)"
)
mycursor=mydb.cursor()
mycursor.execute("Use grocery")
mycursor.execute("Select itemname from grocerylist")
items= mycursor.fetchall()
itemlist={}

    
def start():
    t=True
    while t==True:
        print("===================")
        print("WELCOME TO TERAMART")
        print("===================")
        x=input("Do you have an account with Teramart(yes/no):")
        x.lower()
        if x=="yes":
            global account
            account=0
            account=int(input("Great, please enter your account number:"))
            mycursor.execute("Select * from customer where accountno="+str(account))
            s=mycursor.fetchall()
            if s==[]:
                print("""Your account does not exist. Please either make an account 
                      or enter correct id""")
                continue
            main()
            break
            
        elif x=="no":
            f=input("Would you like to make an account today, it is free of charge(yes/no):")
            f.lower
            if f=="yes":
                account()
                break
            if f=="no":
                print("Ok,Thank you for your time")
                t=False

            else:
                print("Please enter proper response")
                continue
        else:
            print("Please enter proper response")
            continue
        
def main():
    #Option list
    while True:
        print("Enter 1 to make new groceries purchase from TeraMart")
        print("Enter 2 to check previous purchases from TeraMart")
        print("Enter 3 to look at all the items present in store")
        print("Enter 4 to exit menu")
        choice=int(input())
        
        if choice==1:
            #Showing customer all items
            print("All items currently present in TeraMart are:")
            print("Name, price, stock, description")
            mycursor.execute("Select * from grocerylist")
            al = mycursor.fetchall()
            for i in al:
                print(i)
                
            #running function to get grocery list
            groceries()
            
            print("All the items you bought are:")
            print(itemlist)
            print("The total cost of this is:")
            
            #getting total cost of grocery list
            cost=0
            for key in itemlist:
                mycursor.execute("Select price from grocerylist where itemname='"+key+"'")
                val= mycursor.fetchall()
                for i in val:
                    for j in i:
                        zuko=j
                cost+=j*itemlist[key]
                
            print(cost)
            totalcost=cost*1.1
            allitems=''
            tax=cost*0.1

            #Making list of purchase to input in database
            for key in itemlist:
                allitems+=' ' + str(itemlist[key]) + ' '+ str(key)
            amount=(allitems, totalcost, account, tax)    
            print("With tax that is ",str(totalcost))
            mycursor.execute("""Insert into purchases (allitems, totalcost, accountno, tax) values
            (%s,%s,%s,%s)""",amount)
            mydb.commit()
            
        elif choice==2:
            #Showing previous purchases
            mycursor.execute("Select * from purchases where accountno="+str(account))
            use=mycursor.fetchall()
            if use==[]:
                print("You have no previous purchases")
                continue
            
            for i in use:
                print(i)

        elif choice==3:
            #Showing customer all items
            print("All items currently present in TeraMart are:")
            mycursor.execute("Select * from grocerylist")
            ala= mycursor.fetchall()
            for i in ala:
                print(i)
                
        elif choice==4:
            print("""Thank you for choosing TeraMart to make your purchases.
                     I hope you have a good day""")
            break
        
        else:
            print("Please enter a proper value")

def account():
    #Getting customer info
    while True:
        try:
            x=input("Enter your name:")
            y=input("Enter year of birth:")
            if len(y) > 4:
                print("Enter proper value")
            c=input("Enter month of birth in number form(01 is january):")
            d=input("Enter the day of the month:")
            a=y+'-'+c+'-'+d
            phone= input("Enter your phone number:")
            mail= input("Enter your beginning of gmail address without @gmail.com part:")
            address= input("Enter your address:")
            values=(x,a,phone,mail,address)
            
            #Filling it in
            mycursor.execute("""Insert into customer (name, dateofbirth, phonenumber, emailid, address)
                             values (%s,%s,%s,%s,%s)""",values)
            mydb.commit
            mycursor.execute("Select accountno from customer where phonenumber="+phone)
            acc=mycursor.fetchall()
            mycursor.execute("Select * from customer")
            shi=mycursor.fetchall()
            for i in shi:
              print(i)
            #Giving Account number
            print("Your account number is",str(acc))
            print("THANK YOU for making an account with us.")
            main()
            break
        except:
            print("Please enter proper data types")
            continue


        
def groceries():
    h= int(input("Enter the number of unique items you are going to buy:"))
    num=0
    #Getting all items from customer through loop
    while num<h:
          p=input("Enter item to buy:")
          p.lower()
          a=(p,)
          if a not in items: 
              print(items)
              print("Enter proper item name")
              continue
          l=int(input("Enter number of items to buy:"))
          mycursor.execute("Select stock from grocerylist where itemname= '" + p + "'")
          number=mycursor.fetchall()
          for i in number:
              for j in i:
                  sup=j  
          if l>sup:
              print("We only have (%s) of this item in stock. Please choose a smaller amount to buy")
              continue
          num+=1
          alpha=sup-l
          value=(alpha,p)
          #Updating stock amount
          mycursor.execute("Update grocerylist SET stock=(%s) where itemname=(%s)",value)
          mydb.commit()
          itemlist[p]=l
    
if __name__ == '__main__':
   start()

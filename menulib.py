import Cars
import customer
import transaction

def menu_cars():
    while True:
        print("-"*100)
        print("\t\tCAR RECORD MANAGEMENT")
        print("-"*100)
        print("\t\t1. ADD CARS")
        print("\t\t2. DISPLAY ALL CARS")
        print("\t\t3. SEARCH CAR")
        print("\t\t4. UPDATE CAR")
        print("\t\t5. DELETE CAR")
        print("\t\t6. RETURN TO MAIN MENU")
        print("-"*100)
        
        ch=int(input("Enter choice : "))
        print("-"*100)
        print()
        if ch==1:
            Cars.addrecords()
        elif ch==2:
            Cars.showall()
        elif ch==3:
            Cars.searchcars()
        elif ch==4:
            Cars.updatecars()
        elif ch==5:
            Cars.deletecars()
        elif ch==6:
            break
        else:
            print("WRONG CHOICE ENTERED")
            x=print("ENTER ANY KEY")
#menu_cars()

def menu_customer():
    while True:
        print("-"*100)
        print("\t\tMEMBER RECORD MANAGEMENT")
        print("-"*100)
        print("\t\t1. ADD CUSTOMER")
        print("\t\t2. DISPLAY ALL CUSTOMERS")
        print("\t\t3. SEARCH CUSTOMER")
        print("\t\t4. UPDATE CUSTOMER")
        print("\t\t5. DELETE CUSTOMER")
        print("\t\t6. RETURN TO MAIN MENU")
        print("-"*100)
        
        ch=int(input("Enter choice : "))
        print("-"*100)
        print()
        if ch==1:
            customer.addrecords()
        elif ch==2:
            customer.showcustomer()
        elif ch==3:
            customer.searchcustomer()
        elif ch==4:
            customer.updatecustomer()
        elif ch==5:
            customer.deletecustomer()
        elif ch==6:
            break
        else:
            print("WRONG CHOICE ENTERED")
            x=print("ENTER ANY KEY")
#menu_customer()

def menu_transaction():
    while True:
        print("-"*100)
        print("\t\tTRANSACTION RECORD MANAGEMENT")
        print("-"*100)
        print("\t\t1. ADD TRANSACTION")
        print("\t\t2. RETURN TRANSACTION")
        print("\t\t3. DISPLAY TRANSACTION")
        print("\t\t4. DISPLAY TRANSACTION BY CUSTOMER ID")
        print("\t\t5. DISPLAY TRANSACTION BY CARID")
        print("\t\t6. UPDATE TRANSACTION")
        print("\t\t7. DELETE TRANSACTION")
        print("\t\t8. RETURN TO MAIN MENU")
        print("-"*100)
        
        ch=int(input("Enter choice : "))
        print("-"*100)
        print()
        if ch==1:
            transaction.addtransaction()
        elif ch==2:
            transaction.returntransaction()
        elif ch==3:
            transaction.displaytransaction()
        elif ch==4:
            transaction.displaytransactioncustomer()
        elif ch==5:
            transaction.displaytransactioncar()
        elif ch==6:
            transaction.updatetransaction()
        elif ch==7:
            transaction.deletetransaction()
        elif ch==8:
            break
        else:
            print("WRONG CHOICE ENTERED")
            x=print("ENTER ANY KEY")
#menu_transaction()
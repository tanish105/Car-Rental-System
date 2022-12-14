import menulib
print('\t   _____          _____     _____  ______ _   _ _______       _       ')
print('\t  / ____|   /\   |  __ \   |  __ \|  ____| \ | |__   __|/\   | |      ')
print('\t | |       /  \  | |__) |  | |__) | |__  |  \| |  | |  /  \  | |      ')
print('\t | |      / /\ \ |  _  /   |  _  /|  __| | . ` |  | | / /\ \ | |      ')
print('\t | |____ / ____ \| | \ \   | | \ \| |____| |\  |  | |/ ____ \| |____  ')
print('\t  \_____/_/    \_\_|  \_\  |_|  \_\______|_| \_|  |_/_/    \_\______| ')
print('\t                                                                      ')
                                                                     

while True:
    print("-"*100)
    print()
    print("\t\tCAR RENTAL MANAGEMENT SYSTEM")
    print()
    print("-"*100)
    print("\t\t1. CAR MANAGEMENT")
    print("\t\t2. CUSTOMER MANAGEMENT")
    print("\t\t3. TRANSACTION MANAGEMENT")
    print("\t\t4. EXIT")
    print("-"*100)
    
    ch=int(input("Enter your choice : "))
    print("-"*100)
    print()
    if ch ==1:
        menulib.menu_cars()
    elif ch==2:
        menulib.menu_customer()
    elif ch==3:
        menulib.menu_transaction()
    elif ch==4:
        break
    else:
        print("WRONG DETALIS")
        x=intput("ENTER ANY KEY")
import mysql.connector as mycon
from mysql.connector.errors import Error
from mysql.connector import errorcode
con=mycon.connect(host="localhost", user="root",password="tanish",database="CARRENTAL")
cur=con.cursor()
def createtable():
    global con,cur
    cur.execute("create table if not exists transaction(TNo int PRIMARY KEY ,CarID int,CID int,cname varchar(15),DOI date,DOR date,Fine int,TOR int, FOREIGN KEY(CarID) REFERENCES Cars (CarID),FOREIGN KEY(cid) REFERENCES customer(cid))")
    con.commit()
    cur.execute("show tables")
    for x in cur:
        print(x)
#createtable()

def addtransaction():
    global con,cur
    try:
        TNo=int(input('Enter Transaction No. : '))
        CarID=int(input('Enter car id. : '))
        cid=int(input('Enter customer id. : '))
        cname=input("Enter customer name : ")
        DOI=input("Enter date of issue of car : ")
        DOR='0000-00-00'
        Fine=int(input('Enter Fine (caution deposit) : '))
        TOR=int(input("Enter time of rental of car (no. of days) : "))
        query="insert into transaction values(%s,%s,%s,%s,%s,%s,%s,%s)"
        data=(str(TNo),str(CarID),str(cid),cname,DOI,DOR,str(Fine),str(TOR))
        cur.execute(query,data)
        con.commit()
        print('NEW TRANSACTION ADDED SUCCESSFULLY')
        
        query="update cars set Status= 'NOT AVAILABLE' where CarID ='{}'".format(CarID)
        cur.execute(query)
        con.commit()
       
    except ValueError:
        print('Unable to add data because of incorrect data type ')
    except mysql.connector.Error as err:
        if err.errno==errcode.ER_BAD_DB_ERROR:
            print('Wrong database selected ',err)
        elif err.errno==errcode.ER_BAD_TABLE_ERROR:
            print('Wrong table selected')
        else:
            print('Other error',err)
#addtransaction()
            

def returntransaction():
    global con,cur
    TNo=int(input("Enter Transaction number of car to be returned : "))
    print()
    print("************************RETURN TRANSACTION DETAILS****************************")
    query="select * from transaction where TNo={}".format(TNo)
    cur.execute(query)
    results=cur.fetchall()
    if cur.rowcount<=0:
        print("\n#### SORRY! No Matching Details Available####")
    else:
        print('*'*78)
        print('%5s'%'TNo','%5s'%'CarID','%5s'%'CID','%15s'%'Customer Name','%15s'%'DOI','%15s'%'DOR','%5s'%'Fine','%5s'%'TOR')
        print('*'*78)
        for row in results:
            print('%5s'% row[0],'%5s'% row[1],'%5s'% row[2],'%15s'% row[3],'%15s'% row[4],'%15s'%row[5],'%5s'%row[6],'%5s'%row[7])
        print('*'*78)
    ans=input("Are you sure to return(y/n)?")
    if ans=="y" or ans=="Y":
        DOR=input("Enter date of return : ")
        Fine=int(input("Enter Fine Imposed : "))
        query="update transaction set DOR='{}',Fine={} where TNo={}".format(DOR,Fine,TNo)
        cur.execute(query)
        con.commit()
        print("\n##Transaction Updated##")
        
        print()
        print('\t','-'*37)
        print('\t\t       CAR RENTAL')
        print('\t','-'*37)
        print()
        print('\t\t       Tax Invoice')
        print()
        print('\t\t\t     Date :',DOR)
        print('\t  Transaction Number :',TNo)
        print('\t  Car ID :',row[1])
        print('\t  Customer ID :',row[2])
        print('\t  Fine : Dhs.',Fine)
        print()
        print('\t','-'*37)
        print('\t  Mobile No.    : 050-4524242')
        print('\t  Telephone No. : 02-6555313')
        print('\t  Email Id      : carrental@gmail.com')
        print('\t','-'*37)
        
        
#returntransaction()
        
def displaytransaction():
    global con,cur
    print("***************************DISPLAY CARS RENTED********************************")
    query="select * from transaction"
    cur.execute(query)
    results=cur.fetchall()
    if cur.rowcount<=0:
        print("\n#### SORRY! No Matching Details Available####")
    else:
        print('*'*78)
        print('%5s'%'TNo','%5s'%'CarID','%5s'%'CID','%15s'%'Customer Name','%15s'%'DOI','%15s'%'DOR','%5s'%'Fine','%5s'%'TOR')
        print('*'*78)
        cnt=0
        for row in results:
            print('%5s'% row[0],'%5s'% row[1],'%5s'% row[2],'%15s'% row[3],'%15s'% row[4],'%15s'%row[5],'%5s'%row[6],'%5s'%row[7])
            cnt+=1
        print("*"*27,'No of Transactions :',cnt,"*"*27)
   
#displaytransaction()

def displaytransactioncustomer():
    global con,cur
    cid=int(input("Enter customer id to display transaction : "))
    print()
    print("***************************DISPLAY CARS RENTED********************************")
    query="select * from transaction where cid ={}".format(cid)
    cur.execute(query)
    results=cur.fetchall()
    if cur.rowcount<=0:
        print("\n#### SORRY! No Matching Details Available####")
    else:
        print('*'*78)
        print('%5s'%'TNo','%5s'%'CarID','%5s'%'CID','%15s'%'Customer Name','%15s'%'DOI','%15s'%'DOR','%5s'%'Fine','%5s'%'TOR')
        print('*'*78)
        cnt=0
        for row in results:
            print('%5s'% row[0],'%5s'% row[1],'%5s'% row[2],'%15s'% row[3],'%15s'% row[4],'%15s'%row[5],'%5s'%row[6],'%5s'%row[7])
            cnt+=1
        print("*"*27,'No of Transactions :',cnt,"*"*27)
#displaytransactioncustomer()
    
def displaytransactioncar():
    global con,cur
    CarID=int(input("Enter car id to display transaction : "))
    print()
    print("***************************DISPLAY CARS RENTED********************************")
    query="select * from transaction where CarID ={}".format(CarID)
    cur.execute(query)
    results=cur.fetchall()
    if cur.rowcount<=0:
        print("\n#### SORRY! No Matching Details Available####")
    else:
        print('*'*78)
        print('%5s'%'TNo','%5s'%'CarID','%5s'%'CID','%15s'%'Customer Name','%15s'%'DOI','%15s'%'DOR','%5s'%'Fine','%5s'%'TOR')
        print('*'*78)
        cnt=0
        for row in results:
            print('%5s'% row[0],'%5s'% row[1],'%5s'% row[2],'%15s'% row[3],'%15s'% row[4],'%15s'%row[5],'%5s'%row[6],'%5s'%row[7])
            cnt+=1
        print("*"*27,'No of Transactions :',cnt,"*"*27)
#displaytransactioncar()
        

def updatetransaction():
    global con,cur
    TNo=int(input("Enter Transaction number to be updated : "))
    print()
    print("************************UPDATE TRANSACTION DETAILS***************************")
    query="select * from transaction where TNo={}".format(TNo)
    cur.execute(query)
    results=cur.fetchall()
    if cur.rowcount<=0:
        print("\n#### SORRY! No Matching Details Available####")
    else:
        print('*'*78)
        print('%5s'%'TNo','%5s'%'CarID','%5s'%'CID','%15s'%'Customer Name','%15s'%'DOI','%15s'%'DOR','%5s'%'Fine','%5s'%'TOR')
        print('*'*78)
        for row in results:
            print('%5s'% row[0],'%5s'% row[1],'%5s'% row[2],'%15s'% row[3],'%15s'% row[4],'%15s'%row[5],'%5s'%row[6],'%5s'%row[7])
        print('*'*78)
    ans=input("Are you sure to update(y/n)?")
    if ans=="y" or ans=="Y":
        DOR=input("Enter updated date of return : ")
        Fine=int(input("Enter Fine Imposed : "))
        TOR=int(input("enter updated time of rental"))
        query="update transaction set DOR='{}',Fine={},TOR={} where TNo={}".format(DOR,Fine,TOR,TNo)
        cur.execute(query)
        con.commit()
        print("\n##Transaction Updated##")
#updatetransaction()
        
      
def deletetransaction():
    global con,cur
    TNo=int(input("Enter Transaction Number to be deleted : "))
    print()
    print("*****************************DELETE TRANSACTION*******************************")
    query="select * from transaction where TNo={}".format(TNo)
    cur.execute(query)
    results=cur.fetchall()
    if cur.rowcount<=0:
        print("\n##Sorry! No Matching details available##")
    else:
        print('*'*78)
        print('%5s'%'TNo','%5s'%'CarID','%5s'%'CID','%15s'%'Customer Name','%15s'%'DOI','%15s'%'DOR','%5s'%'Fine','%5s'%'TOR')
        print('*'*78)
        for row in results:
            print('%5s'% row[0],'%5s'% row[1],'%5s'% row[2],'%15s'% row[3],'%15s'% row[4],'%15s'%row[5],'%5s'%row[6],'%5s'%row[7])
        print('*'*78)
    ans=input("Are you sure to delete?(y/n)")
    if ans=='y' or ans=='Y':
        query="delete from transaction where TNo={}".format(TNo)
        cur.execute(query)
        con.commit()
        print("\n##Record Deleted##")
#deletetransaction()
        



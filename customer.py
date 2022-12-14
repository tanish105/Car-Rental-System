import mysql.connector as mycon
from mysql.connector.errors import Error
from mysql.connector import errorcode
con=mycon.connect(host="localhost", user="root",password="tanish",database="CARRENTAL")
cur=con.cursor()
def createtable():
    global con,cur
    cur.execute("create table if not exists customer(CID int PRIMARY KEY, cname varchar(25), Mobile int, license int, address varchar(30))")
    con.commit()
    cur.execute("show tables")
    for x in cur:
        print("table name -",x)
#createtable()

def addrecords():
    try:
        global con,cur
        CID=int(input("Enter Customer ID : "))
        cname=input("Enter Customer name : ")
        Mobile=int(input("Enter mobile number : "))
        license=int(input("Enter license number : "))
        ad=input("Enter address of customer : ")
        query="insert into customer values(%s,%s,%s,%s,%s)"
        data=(str(CID),cname,str(Mobile),str(license),ad)
        cur.execute(query,data)
        con.commit()
        print("## DATA SAVED ##")
    except Error as err:
        if err.errno==errorcode.ER_BAD_DB_ERROR:
            print("wrong database",err)
        else:
            print("wrong database 11111",err)
#addrecords()

def showcustomer():
    try:
        global con,cur
        query="Select * from customer"
        cur.execute(query)
        results=cur.fetchall()
        print("*"*80)
        print("%5s" % "CID","%20s" % "Customer Name", "%15s" % "Mobile No.","%15s" % "License No. ","%20s" % "Address")
        print("*"*80)
        cnt=0
        for row in results:
            print("%5s" % row[0],"%20s" % row[1],"%14s" % row[2],"%14s" % row[3],"%22s" % row[4])
            cnt+=1
        print("*"*29,'No of Customers :',cnt,"*"*30)
    except Error as e:
        print("Error",e)

#showcustomer()
        
def searchcustomer():
    global con,cur
    cid=int(input("Enter customer id to search : "))
    print()
    query="select * from customer where CID="+str(cid)
    cur.execute(query)
    result=cur.fetchall()
    if cur.rowcount<=0:
        print("NO MATCHING DETAIL AVAILABLE")
    else:
        print("*"*80)
        print("%5s" % "CID","%20s" % "Customer Name", "%15s" % "Mobile No.","%15s" % "License No. ","%20s" % "Address")
        print("*"*80)
        for row in result:
            print("%5s" % row[0],"%20s" % row[1],"%14s" % row[2],"%14s" % row[3],"%22s" % row[4])
        print("*"*80)
#searchcustomer()
        
def updatecustomer():
    global con,cur
    cid=int(input("Enter customer id to be updated : "))
    print()
    query="select * from customer where CID="+str(cid)
    cur.execute(query)
    result=cur.fetchall()
    if cur.rowcount<=0:
        print("NO MATCHING DETAIL AVAILABLE")
    else:
        print("*"*80)
        print("%5s" % "CID","%20s" % "Customer Name", "%15s" % "Mobile No.","%15s" % "License No. ","%20s" % "Address")
        print("*"*80)
        for row in result:
            print("%5s" % row[0],"%20s" % row[1],"%14s" % row[2],"%14s" % row[3],"%22s" % row[4])
        print("*"*80)
    ans=input("ARE YOU SURE TO UPDATE?(Y/N)")
    if ans in "yY":
        x=input("Enter new Customer name to update : ")
        query="update customer set cname='"+x+"'where CID="+str(cid)
        cur.execute(query)
        con.commit()
        print("RECORD UPDATED")
#updatecustomer()
        
def deletecustomer():
    global con,cur
    cid=int(input("Enter customer id to be deleted : "))
    print()
    query="select * from customer where CID="+str(cid)
    cur.execute(query)
    result=cur.fetchall()
    if cur.rowcount<=0:
        print("NO MATCHING DETAIL AVAILABLE")
    else:
        print("*"*80)
        print("%5s" % "CID","%20s" % "Customer Name", "%15s" % "Mobile No.","%15s" % "License No. ","%20s" % "Address")
        print("*"*80)
        for row in result:
            print("%5s" % row[0],"%20s" % row[1],"%14s" % row[2],"%14s" % row[3],"%22s" % row[4])
        print("*"*80)
    ans=input("ARE YOU SURE TO UPDATE?(Y/N)")
    if ans in "yY":
        query="delete from customer where CID="+str(cid)
        cur.execute(query)
        con.commit()
        print("RECORD DELETED")
#deletecustomer()
        
        


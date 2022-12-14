import mysql.connector as mycon
from mysql.connector.errors import Error
from mysql.connector import errorcode
con=mycon.connect(host="localhost", user="root",password="tanish",database="CARRENTAL")
cur=con.cursor()
def createtable():
    global con,cur
    cur.execute("create table if not exists CARS(CarID int PRIMARY KEY, Carname varchar(25), Price int, Car_Model varchar(20), DOM date, Status varchar(20))")
    con.commit()
    cur.execute("show tables")
    for x in cur:
        print("table name -",x)
#createtable()

def addrecords():
    try:
        global con,cur
        CarID=int(input("Enter car id : "))
        Carname=input("Enter car name : ")
        Price=int(input("Enter price of the car : "))
        Car_Model=input("Enter model name : ")
        DOM=input("Enter date of manufacture : ")
        Status=input("Enter car status : ")
        query="insert into Cars values(%s,%s,%s,%s,%s,%s)"
        data=(str(CarID),Carname,str(Price),Car_Model,DOM,Status)
        cur.execute(query,data)
        con.commit()
        print("## DATA SAVED ##")
    except Error as err:
        if err.errno==errorcode.ER_BAD_DB_ERROR:
            print("wrong database",err)
        else:
            print("wrong database 11111",err)
#addrecords()

def showall():
    try:
        global con,cur
        query="Select * from CARS"
        cur.execute(query)
        results=cur.fetchall()
        print("*"*85)
        print("%5s" % "CarID","%20s" % "Car Name", "%7s" % "Price","%20s" % "Model Name", "%12s" % "DOM","%15s" % "Status")
        print("*"*85)
        cnt=0
        for row in results:
            print("%5s" % row[0],"%20s" % row[1],"%7s" % row[2],"%20s" % row[3],"%12s" % row[4],"%15s" % row[5])
            cnt+=1
        print("*"*34,'No of Cars :',cnt,"*"*35)
    except Error as e:
        print("Error",e)
#showall()
        
def searchcars():
    global con,cur
    carid=int(input("Enter Car ID to search : "))
    print()
    query="select * from Cars where CarID="+str(carid)
    cur.execute(query)
    result=cur.fetchall()
    if cur.rowcount<=0:
        print("NO MATCHING DETAIL AVAILABLE")
    else:
        print("*"*85)
        print("%5s" % "CarID","%20s" % "Car Name", "%7s" % "Price","%20s" % "Model Name", "%12s" % "DOM","%15s" % "Status")
        print("*"*85)
        for row in result:
            print("%5s" % row[0],"%20s" % row[1],"%7s" % row[2],"%20s" % row[3],"%12s" % row[4],"%15s" % row[5])
        print("*"*85)
#searchcars()
        
def updatecars():
    global con,cur
    carid=int(input("Enter Car ID to be updated : "))
    print()
    query="select * from CARS where CarID="+str(carid)
    cur.execute(query)
    result=cur.fetchall()
    if cur.rowcount<=0:
        print("NO MATCHING DETAIL AVAILABLE")
    else:
        print("*"*85)
        print("%5s" % "CarID","%20s" % "Car Name", "%7s" % "Price","%20s" % "Model Name", "%12s" % "DOM","%15s" % "Status")
        print("*"*85)
        for row in result:
            print("%5s" % row[0],"%20s" % row[1],"%7s" % row[2],"%20s" % row[3],"%12s" % row[4],"%15s" % row[5])
        print("*"*85)
    ans=input("ARE YOU SURE TO UPDATE?(Y/N)")
    if ans in "yY":
        x=input("Enter new Car name to update : ")
        query="update CARS set Carname='"+x+"' where CarID="+str(carid)
        cur.execute(query)
        con.commit()
        print("RECORD UPDATED")
#updatecars()

def deletecars():
    global con,cur
    carid=int(input("Enter Car ID to be deleted : "))
    pritn()
    query="select * from CARS where CarID="+str(carid)
    cur.execute(query)
    result=cur.fetchall()
    if cur.rowcount<=0:
        print("NO MATCHING DETAIL AVAILABLE")
    else:
        print("*"*85)
        print("%5s" % "CarID","%20s" % "Car Name", "%7s" % "Price","%20s" % "Model Name", "%12s" % "DOM","%15s" % "Status")
        print("*"*85)
        for row in result:
            print("%5s" % row[0],"%20s" % row[1],"%7s" % row[2],"%20s" % row[3],"%12s" % row[4],"%15s" % row[5])
        print("*"*85)
    ans=input("ARE YOU SURE TO DELETE?(Y/N)")
    if ans in "yY":
        query="delete from CARS where CarID="+str(carid)
        cur.execute(query)
        con.commit()
        print("RECORD DELETED")
#deletecars()


        

        

        
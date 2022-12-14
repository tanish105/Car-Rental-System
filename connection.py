import mysql.connector as mycon
def connect():
    con=mycon.connect(host="localhost", user="root",password="tanish")
    cur=con.cursor()
    print(con.is_connected())
    cur.execute("create database if not exists CARRENTAL")
    print("database created")
    for x in cur:
        print(x)
    cur.close()
    con.close()
connect()
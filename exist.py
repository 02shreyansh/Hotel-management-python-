import mysql.connector
from datetime import date
#global variables
hotel_name =" "
addr =" "
phone=" "
email =" "
gst=0.4
st =5

def clear():
  for _ in range(65):
    print()
clear()

def room_exist():
  mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="hotel")
  mycursor=mydb.cursor()
  sql ="SELECT * FROM rooms;"
  mycursor.execute(sql)
  record = mycursor.fetchall()
  for x in record:
      print(x)
  mydb.commit()

def customer_exist():
  mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="hotel")
  mycursor=mydb.cursor()
  id=int(input("enter customer id>"))
  sql = "SELECT *  from customer where id=%s;"
  mycursor.execute(sql,(id,))
  record = mycursor.fetchall()
  for x in record:
      print(x)
  mydb.commit()
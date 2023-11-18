def search_rooms():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="hotel")
    mycursor=mydb.cursor()
    room_no = input("Enter Room No :")
    sql ="SELECT * FROM rooms WHERE room_no =%s;"
    mycursor.execute(sql,(room_no,))
    record = mycursor.fetchall()
    rec=list(record)
    for x in rec:
        print(x)
    mydb.commit()
    print("Room Status")
    print("*"*120)
    print("Room NO :",record[1:2])
    print("Room Rent :",record[2:3])
    print("Room Bed :",record[3:4])
    print("Room Status :",record[4:5])
    wait=input("\n\n\nPress any key to continue......")

def search_customer():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="hotel")
    mycursor=mydb.cursor()
    print("Search Customer DataBase")
    print("*"*120)
    print("1.   Customer Name")
    print("2.   Customer Address")
    print("3.   Customer Phone")
    print("4.   Customer Email")
    choice = int(input("Enter your choice : "))
    field_name =" "
    if choice ==1:
        name= input("Enter name:")
        sql = "SELECT* FROM customer WHERE name = %s;"
        mycursor.execute(sql,(name,))
        records = mycursor.fetchall()
        for x in records:
            print(x)
    if choice ==2:
        name= input("Enter address:")
        sql = "SELECT* FROM customer WHERE address = %s;"
        mycursor.execute(sql,(name,))
        records = mycursor.fetchall()
        for x in records:
            print(x)
    elif choice ==3:
        name= int(input("Enter phone:"))
        sql = "SELECT* FROM customer WHERE phone = %s;"
        mycursor.execute(sql,(name,))
        records = mycursor.fetchall()
        for x in records:
            print(x)
    elif choice ==4:
        name= input("Enter email:")
        sql = "SELECT* FROM customer WHERE email = %s;"
        mycursor.execute(sql,(name,))
        records = mycursor.fetchall()
        for x in records:
            print(x)
    wait = input("\n\n\nPress any key to continue......")

def search_menu():
    while True:
      clear()
      print(" Search Menu")
      print("*"*120)
      print("\n1.  Room Status")
      print("\n2.  customer Details")
      print("\n3.exit")
      choice = int(input("Enter your choice ...: "))
      if choice==1:
        search_rooms()
      elif choice==2:
        search_customer()
      elif choice==3:
        break
def modify_room():
  mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="hotel")
  mycursor=mydb.cursor()
  print(" Change Room Information ")
  print("*"*120)
  print("1.   Room Type")
  print("2.   Room Rent")
  print("3.   Room Bed")
  choice=int(input('Enter your choice :'))
  field_name=" "
  if choice==1:
    room_type=input("enter room type>>")
    room_no=int(input("Enter room No :"))
    sql="UPDATE rooms SET room_type=%s where  room_no =%s ;"
    val=(room_type,room_no)
    mycursor.execute(sql,val)
    mydb.commit()
  elif choice == 2:
    room_rent=float(input("enter amt.>"))
    room_no=int(input("Enter room No :"))
    sql="UPDATE rooms SET room_rent=%s where  room_no =%s ;"
    val=(room_rent,room_no)
    mycursor.execute(sql,val)
    mydb.commit()
  elif choice==3:
    field_name="room_bed"
    room_bed=input("enter >")
    room_no=int(input("Enter room No :"))
    sql="UPDATE rooms SET room_bed=%s where  room_no =%s ;"
    val=(room_bed,room_no)
    mycursor.execute(sql,val)
    mydb.commit()
  wait = input("\n\n\n Record Updated .............Press any key to continue......")



def modify_customer():
  mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="hotel")
  mycursor=mydb.cursor()
  print(" Change Customer Information ")
  print("*"*120)
  print("1.   Name")
  print("2.   Address")
  print("3.   Phone No")
  print("4.   Email ID")
  print("5.   ID Proof")
  print("6.   ID Proof No")
  print("7.   Males")
  print("8.   Females")
  print("9.   Childeren")
  choice = int(input("Enter your choice :"))
  field_name =" "
  if choice == 1:
    name=input("Enter new name :")
    cust_no = int(input("Enter Customer No :"))
    sql ="UPDATE customer SET name= %s where id =%s;"
    val=(name,cust_no)
    mycursor.execute(sql,val)
    mydb.commit()
  elif choice == 2:
    address=input("Enter new address :")
    cust_no = int(input("Enter Customer No :"))
    sql ="UPDATE customer SET address= %s where id =%s;"
    val=(address,cust_no)
    mycursor.execute(sql,val)
    mydb.commit()
  elif choice==3:
    phone=int(input("Enter new phone :"))
    cust_no = int(input("Enter Customer No :"))
    sql ="UPDATE customer SET phone= %s where id =%s;"
    val=(phone,cust_no)
    mycursor.execute(sql,val)
    mydb.commit()
  elif choice==4:
    email=input("Enter new email :")
    cust_no = int(input("Enter Customer No :"))
    sql ="UPDATE customer SET email= %s where id =%s;"
    val=(email,cust_no)
    mycursor.execute(sql,val)
    mydb.commit()
  elif choice==5:
    id_proof=input("Enter new id_proof :")
    cust_no = int(input("Enter Customer No :"))
    sql ="UPDATE customer SET id_proof= %s where id =%s;"
    val=(id_proof,cust_no)
    mycursor.execute(sql,val)
    mydb.commit()
  elif choice == 6:
    id_proof_no=int(input("Enter new id_proof_no :"))
    cust_no = int(input("Enter Customer No :"))
    sql ="UPDATE customer SET id_proof_no= %s where id =%s;"
    val=(id_proof_no,cust_no)
    mycursor.execute(sql,val)
    mydb.commit()
  elif choice == 7:
    males=int(input("Enter new no. of males :"))
    cust_no = int(input("Enter Customer No :"))
    sql ="UPDATE customer SET males= %s where id =%s;"
    val=(males,cust_no)
    mycursor.execute(sql,val)
    mydb.commit()
  elif choice == 8:
    females=int(input("Enter new no. of females :"))
    cust_no = int(input("Enter Customer No :"))
    sql ="UPDATE customer SET females= %s where id =%s;"
    val=(females,cust_no)
    mycursor.execute(sql,val)
    mydb.commit()
  elif choice == 9:
    children=int(input("Enter new no. of children :"))
    cust_no = int(input("Enter Customer No :"))
    sql ="UPDATE customer SET children= %s where id =%s;"
    val=(children,cust_no)
    mycursor.execute(sql,val)
    mydb.commit()
  wait = input("\n\n\n Record Updated .............Press any key to continue......")
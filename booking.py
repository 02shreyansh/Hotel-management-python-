def room_booking():
  mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="hotel")
  mycursor=mydb.cursor()
  book_id=int(input("enter booking id>"))
  room_id =input("Enter room no to book :")
  cust_id = input("Enter customer ID :")
  date_of_occ = input("Enter date of occupancy (yyyy-mm-dd) :")
  date_of_leave=input("Enter date of leaving(yyyy-mm-dd): ")
  advance = input("Enter advance amount :")
  sql2 ="INSERT INTO  booking VALUES (%s,%s,%s,%s,%s,%s);"
  values=(book_id,room_id,cust_id,date_of_occ,date_of_leave,advance)
  mycursor.execute(sql2,values)
  print("\n\n\nRoom  booked !!!!!!!!")
  mydb.commit()
  wait = input("\n\n\n Press any key to continue....")
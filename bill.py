def bill_generation():
    global gst
    global st
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="hotel")
    mycursor=mydb.cursor()
    room_id = int(input("Enter room no to book :"))
    cust_id = int(input("Enter customer ID :"))
    sql = "SELECT * from booking WHERE cust_id=%s and room_id =%s ;"
    val=(cust_id,room_id)
    mycursor.execute(sql,val)
    record =mycursor.fetchone()
    print(record)
    print("Bill Generation ")
    print("-"*100)
    print(" Rooms occupied  :",room_id)
    dol = date.today()
    book_id = record[0] #book_id_number
    doo = record[3]
    advance = record[5]
    total_days = (dol-doo).days
    result = room_exist()
    rent=int(input("enter rent>>"))
    amount = total_days*rent
    gst_amount = amount*int(gst)/100
    st_amount = amount*int(st)/100
    payable_amount = total_days*rent - advance + gst_amount+st_amount
    print("Date of Occupancy :",doo, "\nDate of Leaving :",dol)
    print("Total Payable Days : ", total_days)
    print("Room Rent Per Day : ", rent)
    print("Total Amount  :",amount)
    print("Advance :",advance,"\nGST ({}) : {} ".format(gst,gst_amount), "\nService Tax ({}) : {}".format(st,st_amount))
    print("Amount Payable :",payable_amount)
    bill_id=int(input("enter bill_id>"))
    book_id=int(input("enter book_id>>"))
    amount=float(input("enter payable_amount>>>"))
    bill_date=input("enter date of bill>")
    gst=int(input("enter gst>>"))
    st=int(input("enter st>>"))
    sql = "INSERT INTO  bill VALUES(%s,%s,%s,%s,%s,%s);"
    values=(bill_id,book_id,amount,bill_date,gst,st)
    mycursor.execute(sql,values)
    mydb.commit()
    wait = input("\n\n\n Press any key to continue....")
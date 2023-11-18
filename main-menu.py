def main_menu():
    while True:
      clear()
      print("H O T E L   M A N A G E M E N T   S Y S T E M ")
      print("*"*120)
      print("\n1.   Add New Room")
      print("\n2.   Add Customer")
      print("\n3.   Modify Room Information")
      print("\n4.   Modify Customer Information")
      print("\n5.   Room Booking")
      print("\n6.   Bill Generation")
      print("\n7.   Search Database")
      print("\n8.   modify_room_status")
      print("\n9.  Close application")
      print("\n\n")
      choice = int(input('Enter your choice ...: '))
      if choice == 1:
            add_room()
      elif choice == 2:
          add_customer()
      elif choice == 3:
          modify_room()
      elif choice == 4:
          modify_customer()
      elif choice ==5 :
          room_booking()
      elif choice == 6:
          bill_generation()
      elif choice ==7 :
          search_menu()
      elif choice == 8:
          change_room_status()
      elif choice ==9:
        print("THANK YOU")
        break
      o=input("do you want to continue.............press Y or y>")
      if o=="N" or o=="n":
          break
main_menu()
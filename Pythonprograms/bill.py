from customer import Order

class biller(Order):

 global discount
 discount = 20

 def bill(self):


    if m.mode_of_payment == 1 and m.item == 2:

     jm = m.quantity
     jk = int(jm) * 20 - discount

     a = open("Hotelbill.txt", "w")
     a.write("****Bill receipt****\n")
     a.write("You have ordered:Vada\n")
     a.write("Quantity is:"+ str(jm) )
     a.write("\nYou have to pay:" + str(jk))
     a.close()


     print("You have ordered:Vada ","Quantity is ", m.quantity)
     print("You have to pay", int(m.quantity) * 20 - discount)

    elif m.mode_of_payment == 1 and m.item == 1:

        jm = m.quantity
        jk = int(jm) * 30 - discount

        a = open("Hotelbill.txt", "w")
        a.write("****Bill receipt****\n")
        a.write("You have ordered:Idly\n")
        a.write("Quantity is:" +str(jm))
        a.write("\nYou have to pay:" + str(jk))
        a.close()

      #print("You have ordered: Idly ", "Quantity is ", m.quantity)
      #print("You have to pay", int(m.quantity) * 30 - discount)

    elif m.mode_of_payment == 1 and m.item == 3:

        jm = m.quantity
        jk = int(jm) * 40 - discount

        a = open("Hotelbill.txt", "w")
        a.write("You have ordered:Vada\n")
        a.write("Quantity is:" + str(jm))
        a.write("\nYou have to pay:" + str(jk))
        a.close()

      #print("You have ordered: Pongal ", "Quantity is ", m.quantity)
      #print("You have to pay", int(m.quantity) * 40 - discount)

    elif m.mode_of_payment == 2 and m.item == 2:

      print("You have ordered vada: ", "Quantity is ", m.quantity)
      print("You have to pay", int(m.quantity) * 20)

    elif m.mode_of_payment == 2 and m.item == 1:

      print("You have ordered Idly: ", "Quantity is ", m.quantity)
      print("You have to pay", int(m.quantity) * 30)

    elif m.mode_of_payment == 2 and m.item == 3:

      print("You have ordered Pongal: ", "Quantity is ", m.quantity)
      print("You have to pay", int(m.quantity) * 40)

    else:
            print("Invalid input")


m = biller()
m.bill()
m.customers()







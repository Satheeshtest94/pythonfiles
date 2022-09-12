from Hotel import restaurant

class Order(restaurant):

 try:

    print("Choose mode of payment", "1.Online", "2.offline")

    mode_of_payment = int(input())

    def customers(self):


            return self.mode_of_payment

 except:

     print("Order class not valid input")





class bus:


    global busticketprice , discount

    busticketprice=100
    discount = 100

    def booking(self, gender, modeoftransport, n, age):

        if gender == "f" and modeoftransport == "bus":
           print("you are identified as female")
           print("you are opted to travel in bus")
           print("You are free to travel")
        elif gender == "m" and modeoftransport == "bus" and age > 58:
             print("you are identified as male")
             print("you have availed ", n, "ticket")
             print("you have to pay Rs", busticketprice * n-discount , "amount (included flat 100)")

        else:
             print("invalid data provided")


print("Some unknown error")
k=bus()
k.booking("00", "bus", 5, 60)




from c2 import process
from c1 import sample


class process2(sample,process):

    def mul(self):

        if c.a <0:
            # Method overriding
            print("Not executed")

    def mul(self):

     if c.a > 0:

         print("Executed")
         print("Multiplication", c.a * c.b)





c = process2()
c.add()
c.sub()
c.mul()

# normal function using ownclass & ownclass.function property
class cl1():


 a = 5
 b = 10


 def add(self):

    self.c = self.a + self.b
    print(self.c)
    # yield c
    #return self.c
"""
 def sub(self):

     d = a - j.c
     print("This is sub",d)
"""
#j = cl1()
#j.add()
#j.sub()

#inheritance within class of same module
class cl2(cl1):

 def sub(self):

     d = j.a - j.c
     print("This is sub",d)

j = cl2()
j.add()
j.sub()







class add():

    global s
    s = 5


    def __init__(self):
        self.m = 1

    def action(self,a,b):
        self.a = a
        self.b = b

        c = self.a +self.b+self.m
        print("Result:",c)

class sub(add):

    def action1(self):
        jk = self.a + self.b + s
        print("inherited:",jk,s)

obj = sub()
#obj.action1(110,20)
obj.action(11,12)



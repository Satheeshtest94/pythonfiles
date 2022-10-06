class a1():



    __a = 5
    _b = 10

    def add(self):

          self.c = self._a + self._b

          print("Addition",self.c)

class b1():

    def sub(self):

        self.d = obj.c - self._b

        print("Sub",self.d)

class c1(a1,b1):

    def div(self):

        m = obj.d / self._b

        print("div", m)

obj = c1()
obj.add()
print(obj.__a)
obj.sub()
obj.div()


"""
class b():

    def sub(self):

        c = a - b

        print("Sub",c)

class c():

    def div(self):

        c = a / b

        print("div", c)


obj = a()
obj.add()
obj = b()
obj.sub()
obj = c()
obj.div()

"""


def reverse():
    return None
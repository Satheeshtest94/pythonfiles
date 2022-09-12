from Base import parent


class fun(parent):

    def process(self):

        if c == "+":
            d = a + b
            print("Your sum value is ", d)
        elif c == "-":
            d = a - b
            print("Your difference value is ", d)
        elif c == "*":
            d = a * b
            print("Your product value is ", d)


obj = fun()
obj.req()
obj.process()

#super keyword using constructor and variable level and method level
class start():
    name = "satheesh"
    def __init__(self,value):
        print("Parent constructor",value)
    def display1(self,value):
        print("from parent:",value)



class end(start):
    name = "kumar"

    def __init__(self):
        super().__init__(50)
        print("child constructor")

    def meth1(self):
        print("Child class parent is start")
    def dispay(self):
        super().display1(100)
        print("using Child:",self.name)
        print("using Child from parent:", super().name)

obj = end()
obj.meth1()
obj.dispay()



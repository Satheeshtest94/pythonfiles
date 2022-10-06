
class data():
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    @property
    def email(self):
        Email = self.fname + self.lname
        return Email


    def cont(self):
        return "Here it is:",self.email


obj  = data("Satheesh","kumar")
print(obj.email)
"""
obj.fname = "Satheesh1"
print(obj.email)
"""
obj.cont()

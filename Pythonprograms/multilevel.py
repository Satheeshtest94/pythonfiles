class check():

    
    _d = 112

    def add(self, a, b,_d):

        self.a = a
        self.b = b
        self._d =_d

        self.c = self.a+ self.b +self._d
        print(self.c)

ob = check()
ob.add(5,6)
#print(ob.a)
#print(ob.d)

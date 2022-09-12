from abc import ABC,abstractmethod

class abs(ABC):
    @abstractmethod
    def add(self):
        return 0

class size(abs):
    def add(self):
       c = 5 + 6
       print(c)
       return c




obj = size()
obj.add()
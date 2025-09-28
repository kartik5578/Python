from abc import ABC, abstractmethod

class Claulation(ABC):

    @abstractmethod
    def sum(self, a, b):
        pass

    def print_walla(self):
        print("Wallla")

class sumation(Claulation):

    def print_a(self):
        print("thdhsa")

    def sum(self, a, b):
        return a+b
    


s = sumation()


print(s.sum(2, 5))
s.print_walla()

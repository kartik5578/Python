class Complex:

    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    # def __eq__(self, other):
    #     if(self.n1 == other.n1 and self.n2==other.n2):
    #         return True
    #     else:
    #         return False

    def printcomplex(self):
        print(self.n1, "+", self.n2,"i")


c1 = Complex(2, 5)
c2 = Complex(2, 5)

if(c1==c2):
    print("Equal")
else:
    print("Not Equal")

c1.printcomplex()
class Parent:
    def skills(self):
        print("Parent: Parenting")

class Father(Parent):
    pass
    def skills(self):
        print("Father: Cooking")

class Mother(Parent):

    def skills(self):
        print("Mother: Painting")

class Child(Father, Mother):
    pass
    def skill(self):
        print("Child: Dancing")

c = Child()
p = Father()
c.skills()   
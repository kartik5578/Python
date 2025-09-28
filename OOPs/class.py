class employee:

    #class or static variable
    company = "EPAM"

    def __init__(self, id, name):
        self.id = id
        self.name = name
        print("Employee details saved successfully")

    def printemp(self):
        print("Employee Id:", self.id ,"\nEmployee Name:", self.name, "\nEmployee Company:", self.company, "\n")

    def compareid(self, other):
        if self.id == other.id:
            print("Same")
        else:
            print("differnet")

    def compare(self, other):
        if self == other:
            print("Same")
        else:
            print("differnet")



emp = employee(5, "Kartik")
emp4 = emp
emp2 = employee(2, "Sakshi")
emp3 = employee(8, "sruthi")
# print(type(emp))
# employee.config(emp)
# employee.company = "Google"
emp.printemp()
emp2.printemp()
emp3.printemp()



emp.compareid(emp3)
emp.compare(emp4)



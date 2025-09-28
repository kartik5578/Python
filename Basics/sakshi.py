class Sakshi:
    
    name = "Sakshi Jagtap"

    def __init__(self, age, sal):
        self.age = age
        self.sal = sal

    def print_info(self):
        print('Name:',self.name, '\nAge:', self.age, '\nSalaray:', self.sal)


    def increase_sal(self, increment, bonus_per):
        bonus = self.sal* bonus_per
        total_sal = self.sal + increment+ bonus
        print(total_sal)

class Employee(Sakshi):
    def __init__(self, age, sal, role):
        super().__init__(age, sal)
        self.role = role

    def assiged_proj(self, is_assigned):
        is_assigned = is_assigned.lower()
        
        if is_assigned == 'yes':
            return True
        elif is_assigned =='no':
            return False
        else:
            return 'Enter valid input'
    
    def increase_sal(self, increment, bonus_per):
        bonus = self.sal* bonus_per
        total_sal = self.sal * increment+ bonus
        print(total_sal)



s = Sakshi(22, 60000)
# print(s.name)
# s.print_info()


s.increase_sal(10000, 0.2)


obj = Employee(22,60000, 'Application support')
obj2 = Employee(20,50000, 'Dveloper')
obj3 = Employee(24,30000, 'Analyst')


# proj_assign = obj.assiged_proj('no')

# if(proj_assign == True):
#     print("Proj is assigned")
# elif(proj_assign == False):
#     print("Proj is not assigned")
# else:
#     print(proj_assign)


s.increase_sal(1000000, 0.8)


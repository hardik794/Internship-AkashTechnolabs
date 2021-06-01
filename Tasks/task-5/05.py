class Employee:
    name ="ABCDEFG"
    designation ="HR Manager"
    def display(self):
        print('name : ',self.name)
        print('designation : ',self.designation)

class Subclass(Employee):
    salary=10000
    def display(self):
        print('name : ',self.name)
        print('designation : ',self.designation)
        print('salary : ',self.salary)


obj1 = Employee()
obj2 = Subclass()
print('-------Employee class display()-------')
obj1.display()
print("-------Subclass display()---------")
obj2.display()
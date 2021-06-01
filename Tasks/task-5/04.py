import math
class Cal4:
    def setdata(self,num):
        self.num = num
    
    def display(self):
        square = self.num**2
        return square

obj = Cal4()
value = int(input("enter any number:"))
obj.setdata(value)
print("square of value {} is {}".format(value,obj.display()))
import math
class Cal2:
    def setdata(self,radius):
        self.radius =radius
    def display(self):
        area = math.pi*self.radius*self.radius
        print('Area of circle with radius {} ={:.2f}'.format(self.radius,area))


obj = Cal2()
obj.setdata(3)
obj.display()
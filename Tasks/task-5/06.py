class Cal5:
    def __init__(self,height,width):
        self.length = lenght
        self.width = width
    
    def calArea(self):
        area = self.length * self.width
        print("Area of rectangle with length={} and width ={} is {}".format(self.length,self.width,area))

lenght =int(input("enter length:"))
width =int(input("enter width:"))

obj = Cal5(lenght,width)
obj.calArea()
class Cal1:
    def setdata(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def display(self):
        sum =self.a+self.b+self.c
        print("{}+{}+{} = {}".format(self.a,self.b,self.c,sum))


obj = Cal1()
obj.setdata(10,20,30)
obj.display()
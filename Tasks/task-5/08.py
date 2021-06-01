class Publisher:
    title_name ="John Carter"
    def display(self):
        print("Name : ",self.title_name)
class book(Publisher):
    no_pages = 200
    def display(self):
        print("Name : ",self.title_name)
        print('Pages:',self.no_pages)

class tape(book):
    time = 3
    def display(self):
        print("Name : ",self.title_name)
        print('Pages:',self.no_pages)
        print('time :{} hrs'.format(self.time))

obj1 = Publisher()
obj2 = book()
obj3 = tape()
print("----Publisher display()----")
obj1.display() 
print("----Book display()----")
obj2.display() 
print("----Tape display()----")
obj3.display() 
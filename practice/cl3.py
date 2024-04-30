class Shape():
    def __init__(self):
        self.area=0
    def printArea(self):
        print(self.area)
class Square(Shape):
    def __init__(self,length):
        super().__init__()
        self.length=length
        self.area=self.length**2
class Rectangle(Shape):
    def __init__(self,length,width):
        super().__init__()
        self.length=length
        self.width=width
        self.area=self.length*self.width
s=input()
l=s.split()
x=Rectangle(int(l[0]), int(l[1]))
x.printArea()
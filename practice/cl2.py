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
    
x=Square(int(input()))
x.printArea()
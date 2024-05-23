import math
class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.copy_x=x
        self.copy_y=y
    def move(self,other):
        dx=self.copy_x+other.copy_x
        dy=self.copy_y+other.copy_y
        return str(dx)+' '+str(dy)
    def distance(self, other):
        dx=self.x-other.x
        dy=self.x-other.x
        return math.sqrt(dx**2+dy**2)
s=input()
l=s.split()
a=input()
b=a.split()
x=Point(int(l[0]),int(l[1]))
y=Point(int(b[0]),int(b[1]))
print(x.move(y))
print(x.distance(y))
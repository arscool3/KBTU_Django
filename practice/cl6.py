import math
class FilterPrime():
    def __init__(self,array):
        self.array=array
    def Filter(self,maxi):
        for i in range(2,int( math.ceil(math.sqrt(maxi)) )):
            self.array=list(filter(lambda x:x==i or x%i , self.array))
        for i in self.array:
            print(i,end=' ')
s=input()
l=s.split()
l=[int(x) for x in l]
maxi=int(max(l))
x=FilterPrime(l)
x.Filter(maxi)
import math
def filter_prime(l):
    maxi=int(max(l))
    for i in range(2,int(math.ceil(maxi**0.5))):
        l=list(filter(lambda x:x==i or x%i,l))
    for i in l:
        print(i,end=' ')
s=input()
l=s.split()
l=[int(x) for x in l]
filter_prime(l)
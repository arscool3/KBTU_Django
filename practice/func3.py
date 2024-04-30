def solve(heads,legs):
    x=int((legs-2*heads)/2)
    y=int(heads-x)
    print(str(y)+' '+str(x))
x,y=map(int,input().split())
solve(x, y)
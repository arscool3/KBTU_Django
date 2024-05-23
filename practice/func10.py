def unique(l):
    p=[]
    for x in l:
        if x not in p:
            p.append(x)
    return p
s=input()
l=s.split()
print(unique(l))

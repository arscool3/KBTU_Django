def has_33(nums,ok):
    for x in range(0,len(nums)-1):
        if nums[x]==3 and nums[x+1]==3:
            ok=True
    return ok
s=input()
l=list(s)
l=[int(x) for x in l]
ok=False
print(has_33(l,ok))
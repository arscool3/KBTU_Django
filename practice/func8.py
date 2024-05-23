def has_007(nums,ok):
    for x in range(0,len(nums)-1):
        if nums[x]==0 and nums[x+1]==0 and nums[x+2]==7:
            ok=True
    return ok
s=input()
l=s.split()
l=[int(x) for x in l]
ok=False
print(has_007(l,ok))
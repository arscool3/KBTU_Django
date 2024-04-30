def histogram(nums):
    for x in range(0,len(nums)):
        for y in range(0,nums[x]):
            print('*',end='')
        print('')
s=input()
l=s.split()
l=[int(x) for x in l]
histogram(l)
def reverse(string_list,size):
    for x in range(size-1,-1,-1):
        print(string_list[x],end=' ')
s=input()
l=s.split()
size=len(l)
reverse(l, size)

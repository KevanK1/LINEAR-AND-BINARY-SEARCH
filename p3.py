def FindInList(num, l):
    if len(l)==0:
        return -1
    pos=-1
    for i in range(0,len(l)):
        if l[i]==num:
            pos=i
            break
    return pos
l=[11,2,44,5,1,87,7]
l2=[]
print(FindInList(2,l))

print(FindInList(2,l2))
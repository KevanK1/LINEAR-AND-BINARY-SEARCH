# Find the maximum number in a list
def maxNumInList(l):
    if len(l)==0:
        return -1
    max= l[0]
    for i in l:
        if max < i:
            max = i
    return max

def minNumInList(l):
    if len(l)==0:
        return -1
    min= l[0]
    for i in l:
        if min > i:
            min = i
    return min

l=[11,2,44,5,1,87,7]

print(maxNumInList(l))
print(minNumInList(l))

# OR U CAN JUST 

print(max(l))
print(min(l))
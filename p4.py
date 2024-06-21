from typing import List
# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
class Solution:
    def countDigit(self,num):
        if num==0:
            return 1
        i=0
        while num:
            num=num//10
            i+=1
        return i


    def findNumbers(self, l: List[int]) -> int:
        if len(l)==0:
            return -1
        x=0
        for i in l:
            if self.countDigit(i)%2==0:
                x+=1
        return x
l=[[1,2],[1,2,3]]
# print(l[1][2])

for i in range(0,len(l)):
    for j in range(0,len(l[i])):
        print(l[i][j],end=" ")
    print("ṆN")
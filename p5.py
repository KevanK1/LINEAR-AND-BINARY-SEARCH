from typing import List
# https://leetcode.com/problems/richest-customer-wealth/submissions/1295289942/
class Solution:
    def countWealth(self, l: List[int]) -> int:
        if len(l)==0:
            return -1
        sum=0
        for i in l:
            sum+=i
        return sum

    def maximumWealth(self, accounts: List[List[int]]) -> int:
        if len(accounts)==0:
            return -1
        max= self.countWealth(accounts[0])
        
        for i in range(0,len(accounts)):
            if max< self.countWealth(accounts[i]):
                max= self.countWealth(accounts[i])
        return max

# USING sum()
# class Solution:
#     
#     def maximumWealth(self, accounts: List[List[int]]) -> int:
#         if len(accounts)==0:
#             return -1
#         max= self.sum(accounts[0])
        
#         for i in range(0,len(accounts)):
#             if max< self.sum(accounts[i]):
#                 max= self.sum(accounts[i])
#         return max
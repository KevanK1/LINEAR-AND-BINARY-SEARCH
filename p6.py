from typing import List
# https://leetcode.com/problems/find-target-indices-after-sorting-array/
class Solution:
    def targetIndices(self, l: List[int], target: int) -> List[int]:
        if len(l)==0:
            return []
        if target not in l:
            return []
        lis=[]
        l= sorted(l)
        for i in range(0,len(l)):
            if l[i]==target:
                lis.append(i)
        return lis
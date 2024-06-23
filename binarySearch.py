class Solution:
    def search(self, l: List[int], tar: int) -> int:
        if len(l)==0:
            return -1
        if tar<l[0] or tar>l[-1]:
            return -1
        start=0
        end=len(l)-1
        
        while(start<=end):
            n= (start+end)//2
            if l[n]==tar:
                return n
            elif tar < l[n]:
                end= n-1
            else:
                start=n+1
        return -1
        

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        dum=nums.copy()
        dum=sorted(dum)
        l=len(dum)
        lind= True
        a=0
        b=0
        for i in range(l):
            if lind:
                if nums[i]!=dum[i]:
                    lind=False
                    a=i
            if nums[i]!=dum[i]:
                b=i
        if lind==False:        
            return b-a+1 
        return 0
            
            
                    
                    
            
        
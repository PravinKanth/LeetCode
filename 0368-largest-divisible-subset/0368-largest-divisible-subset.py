class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        a=sorted(nums)
        b=[[i] for i in a]
        l=len(a)
        for i in range(l):
            for j in range(i):
                if a[i]%a[j]==0 and len(b[i])<len(b[j])+1:
                    b[i]=b[j]+[a[i]]
        return max(b,key=len)                       
                    
        
                    
                
        
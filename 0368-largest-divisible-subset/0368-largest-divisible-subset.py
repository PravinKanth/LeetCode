class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        a=sorted(nums)
        ans=[[i] for i in a]
        l=len(a)
        for i in range(l):
            for j in range(i):
                if a[i]%a[j]==0 and len(ans[i])<=len(ans[j]):
                    ans[i]=[a[i]]+ans[j]
        max1=0
        lst=[]
        for i in ans:      
            if len(i)>max1:
                max1=len(i)
                lst=i
        return lst        
                
                     
                    
        
                    
                
        
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a=[1]*len(nums)
        b=1
        for i in range(1,len(nums)):
            b*=nums[i-1]
            a[i]=b
        b=1
        for j in range(len(nums)-1,0,-1):
            b*=nums[j]
            a[j-1]*=b
        return(a)
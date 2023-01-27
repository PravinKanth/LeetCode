class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        arr=[0]*k
        part=sum(nums)/k
        nums=sorted(nums,reverse=True)
        l=len(nums)
        
        def func(i):
            if i==l:
                return len(set(arr))==1
            for j in range(k):
                arr[j] += nums[i]
                if arr[j] <= part and func(i+1):
                    return True
                arr[j] -= nums[i]
                if arr[j] == 0:
                    break
            return False        
        
        return func(0)
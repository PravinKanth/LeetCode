class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans={}
        for i in range(0,len(nums)):
            if nums[i] not in ans:
                ans[target-nums[i]]=i
            else:
                return ans[nums[i]],i
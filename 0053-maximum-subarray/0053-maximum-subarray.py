class Solution:
    def maxSubArray(self, nums):
        cur=0
        max1=float("-inf")
        for i in nums:
            cur=max(i, cur + i)
            max1 = max(max1, cur)
        return max1
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans=[]
        sum1=0
        for i in nums:
            sum1+=i
            ans.append(sum1)
        return ans
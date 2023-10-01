class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        lis=[]
        nums=sorted(nums)
        for i,j in enumerate(nums):
            if j == target:
                lis.append(i)
        return lis        
        
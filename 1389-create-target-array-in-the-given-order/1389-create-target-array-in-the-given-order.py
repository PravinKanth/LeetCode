class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        lst=[]
        for i,j in zip(nums,index):
            lst[j:j]=[i]
        return lst    
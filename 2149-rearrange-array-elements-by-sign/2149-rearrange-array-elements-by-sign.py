class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        l = len(nums)
        lst = [0] * l
        e = 0
        o = 1
        for i in nums:
            if i>0:
                lst[e]=i
                e+=2
            else:
                lst[o]=i
                o+=2
        return(lst)
        
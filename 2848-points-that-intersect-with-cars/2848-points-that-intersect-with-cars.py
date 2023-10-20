class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        lst=set()
        for i in nums:
            for j in range(i[0],i[1]+1):
                lst.add(j)
        return len(lst)        

        
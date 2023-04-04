class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d=defaultdict(int)
        sum1=0
        for i in nums:
            d[i]+=1
        for i in d.values():
            sum1+=i*(i-1)/2
        return int(sum1)    
            
            
        
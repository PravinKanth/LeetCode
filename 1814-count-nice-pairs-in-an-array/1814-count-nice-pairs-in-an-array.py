class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        map={}
        for i in nums:
            rev=str(i)[::-1]
            rev=int(rev)
            if i-rev not in map:
                map[i - rev]=1
            else:
                map[i - rev]+=1
        co=0
        for i in map:
            if map[i]>=2:
                co+=(map[i]*(map[i]-1))/2
        return(int(co)%(1000000000+7))
        
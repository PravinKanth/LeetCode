
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        counter =Counter(nums)
        dict = collections.defaultdict(int)
        for i in nums:
            if counter[i]:
                counter[i]-=1
                if dict[i-1]:
                    dict[i]+=1
                    dict[i-1]-=1
                elif counter[i+1] and counter[i+2]:
                    counter[i+2]-=1
                    counter[i+1]-=1
                    dict[i+2] +=1
                else:
                    return False
        return True
class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        ls=0
        rs=sum(nums)-nums[0]
        i=0
        ans=[abs(sum(nums)-nums[0]-0)]
        for _ in range(len(nums)-1):
            ls+=nums[i]
            rs-=nums[i+1]
            i+=1
            ans.append(abs(ls-rs))
        return ans    
            
        
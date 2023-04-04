class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        j=n
        ans=[]
        for i in range(j):
            ans.append(nums[i])
            ans.append(nums[j])
            j+=1
        return ans         
            
        
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        dic={}
        for i in nums1:     
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
            if i in nums2 and nums2.count(i)>=dic[i]:
                ans.append(i)   

                        
                           
        return ans        
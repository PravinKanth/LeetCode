class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash={}
        maxi=0
        point=0
        for i in range(len(s)):
            if s[i] in hash and point<=hash[s[i]]:
                point=hash[s[i]]+1
            else:
                maxi=max(maxi,i-point+1)
            hash[s[i]]=i  

        return maxi          


              


                



            


                

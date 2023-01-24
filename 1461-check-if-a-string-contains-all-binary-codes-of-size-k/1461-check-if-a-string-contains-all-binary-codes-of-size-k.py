class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        ans=set()
        l=len(s)
        for i in range(l-k+1):
            ans.add(s[i:i+k])
        if len(ans)==2**k:
            return(True)
        return(False)
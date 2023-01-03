class Solution:
    def longestPrefix(self, s: str) -> str:
        l=0
        i=1
        lp=[0]*len(s)
        while(i<len(s)):
            if s[i]==s[l]:
                l+=1
                lp[i]=l
                i+=1
            else:
                if l!=0:
                    l=lp[l-1]
                else:
                    lp[i]=0
                    i+=1   
        max1=lp[len(lp)-1]
        st=""
        for i in range(max1):
            st+=s[i]
        return st    






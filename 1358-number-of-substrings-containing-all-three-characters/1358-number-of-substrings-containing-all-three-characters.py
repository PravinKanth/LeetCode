class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        a=-1
        b=-1
        c=-1
        l=len(s)
        sum1=0
        for i in range(l):
            if s[i]=='a':
                a=i
            elif s[i]=='b':
                b=i
            else:
                c=i
            sum1+=min(a,b,c)+1
        return(sum1)



        
        
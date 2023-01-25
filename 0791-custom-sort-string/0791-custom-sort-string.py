class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ans=""
        dict=defaultdict(int)
        for i in s:
            dict[i]+=1
        for i in order:
            if i in s:
                while(dict[i]!=0):
                    ans+=i
                    dict[i]-=1
        for i in s:
            if i not in order:
                ans+=i
        return(ans)
        
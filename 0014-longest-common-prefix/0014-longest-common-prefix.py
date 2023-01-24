class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        a=sorted(strs,key=len)[0]
        count=0
        l=len(strs)
        ini=-1
        flag=True
        for i in a: 
            count=0
            ini+=1
            if flag==False:
                break
            for j in strs:
                if j[ini]==a[ini]:
                    count+=1
            if count==l:
                ans+=j[ini]
            else:
                flag=False
                
        return ans        
        
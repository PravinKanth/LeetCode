class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        n=rowIndex
        ans=[]
        for i in range(1,n+2):
            ans.append([0]*i)
        for i in range(n+1):
            for j in range(i+1):
                if(j==0 or j==i):
                    ans[i][j]=1
                else:
                    ans[i][j]=ans[i-1][j-1]+ans[i-1][j]
        return ans[n]
        
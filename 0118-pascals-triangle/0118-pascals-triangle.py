class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n=numRows
        ans=[]
        for i in range(1,n+1):
            ans.append([0]*i)
        for i in range(n):
            for j in range(i+1):
                if(j==0 or j==i):
                    ans[i][j]=1
                else:
                    ans[i][j]=ans[i-1][j-1]+ans[i-1][j]
        return ans
        
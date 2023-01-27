class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        ans=[0]*(k+maxPts)
        sumans=0
        for i in range(k+maxPts-1,k-1,-1):
            if i<=n:
                ans[i]=1
            sumans+=ans[i]
        for i in range(k-1,-1,-1):
            ans[i]=sumans/maxPts;
            sumans+=ans[i]
            sumans-=ans[i+maxPts]
        return ans[0]
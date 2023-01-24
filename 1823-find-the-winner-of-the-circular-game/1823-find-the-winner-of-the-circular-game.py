class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def func(n,k):
            if n==1:
                return 1
            else:
                return (func(n-1,k)+k-1)%n+1
        return(func(n,k))
        
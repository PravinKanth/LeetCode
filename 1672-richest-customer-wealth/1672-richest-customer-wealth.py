class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        fun=lambda x:sum(x)
        max1=0
        for i in accounts:
            if(fun(i))>max1:
                max1=fun(i)
        return max1        
        
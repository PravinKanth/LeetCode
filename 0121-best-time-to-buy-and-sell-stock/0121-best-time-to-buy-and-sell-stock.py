class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min1=prices[0]
        maxi=0
        for i in prices:
            if i <min1:
                min1=i
            if i >min1:
                if i-min1>maxi:
                    maxi=i-min1 
        return maxi            




        



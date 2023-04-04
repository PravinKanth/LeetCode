class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxv=max(candies)
        lst=[]
        for i in candies:
            if i+extraCandies>=maxv:
                lst.append(True)
            else:
                lst.append(False)
        return lst        
                
        
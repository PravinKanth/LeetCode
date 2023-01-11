class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        l=len(cards)
        m={}
        max1=l+1
        for i in range(l):
            if cards[i] not in m:
                m[cards[i]]=i
            else:
                t=i-m[cards[i]]+1
                if t<max1:
                    max1=t
                m[cards[i]]=i    
        if max1==l+1:
            return -1
        return max1        

                    
                
                    
        
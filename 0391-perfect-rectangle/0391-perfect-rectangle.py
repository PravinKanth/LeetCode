class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        dum= set()
        sum1 = 0
        for x,y,a,b in rectangles:
            sum1+=(a-x)*(b-y)
            dum^={(x,y),(a,b),(x,b),(a,y)}
        if dum:    
            llst = sorted(dum)[0]
            rlst = sorted(dum)[-1]
            totalarea = (rlst[0] - llst[0]) * (rlst[1] - llst[1])
        else:
            totalarea=0    
        if totalarea==sum1 and len(dum)==4:
            return(True)
        return False
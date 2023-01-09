class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        lst=[]
        def calc(a,b):
            if math.sqrt(((b[1]-a[1])*(b[1]-a[1]))+((b[0]-a[0])*(b[0]-a[0]))) not in lst:
                lst.append(math.sqrt(((b[1]-a[1])*(b[1]-a[1]))+((b[0]-a[0])*(b[0]-a[0]))))
        if p1!=p2 and p1!=p3 and p1!=p4 and p2!=p3 and p2!=p4 and p3!=p4:  
            calc(p1,p2)
            calc(p1,p3)
            calc(p1,p4)
            calc(p2,p3)
            calc(p2,p4)
            calc(p3,p4)
            if len(lst)==2:
                return True
            return False
        return False
        
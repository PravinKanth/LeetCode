class Solution:
    def reverse(self, x: int) -> int:
        x=str(x)
        i=0
        if x[0]=="-":
            i=-int(x[1:][::-1])
        else:
            i=int(x[0:][::-1])
        if i<-2**31 or i>2**31-1:
            return 0
        return i
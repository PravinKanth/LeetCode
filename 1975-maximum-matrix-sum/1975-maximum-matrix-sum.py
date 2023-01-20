class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        cnt=0
        tcnt=0
        min1=float("inf")
        for i in matrix:
            for j in i:
                if abs(j) <= min1:
                    min1 = abs(j)
                if j<0:
                    cnt+=1
                tcnt+=abs(j)
        sol=0
        if cnt%2==0:
            for i in matrix:
                for j in i:
                    sol+=abs(j)
        else:
            sol=tcnt-(2*(min1))
        return(sol)
        
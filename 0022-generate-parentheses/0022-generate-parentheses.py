class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(fin, s, l, r):
            if l==0 and r==0:
                fin.append(s)
                
            if l>0:
                helper(fin, s+'(', l-1, r)
                
            if r>0 and l<r:
                helper(fin, s+')', l, r-1)
        
        fin = []
        helper(fin, '', n, n)     
        return fin
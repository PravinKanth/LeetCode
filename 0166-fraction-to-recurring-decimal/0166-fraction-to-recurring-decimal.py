import collections
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign="-" if(numerator*denominator<0) else ''
        numerator,denominator=abs(numerator),abs(denominator)
        
        q,r=divmod(numerator, denominator)
        if not r:
            return sign+str(q)
        dict=collections.defaultdict(int)
        re=[sign+str(q)+'.']
        ind=len(re)
            
        while r:
            q,r=divmod(r*10, denominator)
            if (q,r) not in dict:
                dict[(q,r)]=ind
                re.append(str(q))
                ind+= 1
            else:
                ind=dict[(q,r)]
                re[ind]='('+re[ind]
                re[-1]=re[-1]+')'
                break
                
        return ''.join(re)
        
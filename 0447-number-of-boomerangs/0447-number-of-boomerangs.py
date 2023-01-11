class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        l=len(points)
        count=0
        for i in range(l):
            m={}
            for j in range(l):
                if i==j:
                    continue
                else:
                    a=(points[j][0]-points[i][0])*(points[j][0]-points[i][0])+(points[j][1]-points[i][1])*(points[j][1]-points[i][1])
                    if a not in m:
                        m[a]=1
                    else:
                        m[a]+=1
            for k in m:
                if m[k]>=2:
                    count+=(m[k]*(m[k]-1))
        return count            
        
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals)
        li=[]
        prevstart=intervals[0][0]
        prevend=intervals[0][1]
        l=len(intervals)
        for i in range(1,l):
            if (prevend >=intervals[i][0] and prevend<=intervals[i][1]) :
                current=[prevstart,intervals[i][1]]
                prevstart=prevstart
                prevend=intervals[i][1]
            elif(prevend >=intervals[i][0] and prevend>=intervals[i][1]):
                current = [prevstart, prevend]
                prevstart = prevstart
                prevend = prevend

            else:
                li.append([prevstart,prevend])
                prevstart=intervals[i][0]
                prevend=intervals[i][1]
        li.append([prevstart,prevend])
        return(li)
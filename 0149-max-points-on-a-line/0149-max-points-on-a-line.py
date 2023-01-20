class Solution:
    def maxPoints(self, p: List[List[int]]) -> int:
        n = len(p)
        if n == 1:
            return 1
        ans = 1
        count = collections.Counter()
        a = 0
        for i in range(n):
            count.clear()
            for j in range(n):
                if j != i:
                    a = p[j][0] - p[i][0]
                    if a:
                        count[(p[j][1] - p[i][1]) / a] += 1
                    else:
                        count[None] += 1

            ans = max(ans, max(count.values()))
        return ans + 1
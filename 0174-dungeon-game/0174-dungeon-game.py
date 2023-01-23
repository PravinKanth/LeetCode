class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        ans = [[float('inf') for _ in range(n)] for i in range(m)]
        
        
        def func(i, j):
            if i == m-1 and j == n-1:
                ans[i][j] = max(1, 1 - dungeon[i][j])
                return ans[i][j]
            
            if ans[i][j] != float('inf'):
                return ans[i][j]
            
            right = down = float('inf')
            if i < m-1:
                down = max(1, func(i+1, j) - dungeon[i][j])
            if j < n-1:
                right = max(1, func(i, j+1) - dungeon[i][j])
                
            ans[i][j] = min(right, down)
            return ans[i][j]
            
        return func(0, 0)
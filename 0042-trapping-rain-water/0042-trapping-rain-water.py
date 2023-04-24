class Solution:
    def trap(self, height: List[int]) -> int:
        sumv = 0
        n = len(height)
        lst=[0]*n
        lst[n-1] = height[n - 1]
        for i in reversed(range(n-1)):
            lst[i] = max(lst[i+1],height[i])
        left = height[0]
        for i in range(1, n-1):
            left = max(left, height[i])
            diff = min(left, lst[i]) - height[i]
            sumv += diff
        return sumv
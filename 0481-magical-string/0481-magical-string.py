class Solution:
    def magicalString(self, n: int) -> int:
        lst = [1, 2, 2]
        i = 2
        while len(lst) < n:
            lst.append(3 - lst[-1])
            if lst[i] == 2:
                lst.append(lst[-1])
            i += 1
        
        count = 0
        for i in range(n):
            if lst[i] == 1:
                count += 1
        return count
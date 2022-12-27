class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        for i in range(n):
            for j in range(i+1):
                t = s[j:(n-i+j)]
                if t==t[::-1]:
                    return t  

class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=""
        for i in s:
            if i.isalnum():
                st+=i.upper()
        if st==st[::-1]:
            return True
        return False
        
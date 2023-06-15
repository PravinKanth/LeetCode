class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a="".join(sorted(list(s)))
        b="".join(sorted(list(t)))
        if a==b:
            return True
        return False
        
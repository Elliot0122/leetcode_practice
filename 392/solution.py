class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx1 = 0
        idx2 = 0

        while idx1 < len(s) and idx2 < len(t):
            if s[idx1] == t[idx2]:
                idx1+=1
            idx2+=1

        if idx1 == len(s):
            return True
        else:
            return False

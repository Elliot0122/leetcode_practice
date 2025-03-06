class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        chars = set()
        occur = dict()
        for i in range(len(s)):
            if s[i] not in chars:
                chars.add(s[i])
                occur[s[i]] = 1
            else:
                occur[s[i]] += 1
            if t[i] not in chars:
                chars.add(t[i])
                occur[t[i]] = -1
            else:
                occur[t[i]] -= 1
        
        for char in list(chars):
            if occur[char] != 0:
                return False
        else:
            return True

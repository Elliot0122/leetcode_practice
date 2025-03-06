class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        if len(s) != len(pattern): return False
        pattern1 = dict()
        pattern2 = dict()
        length = len(pattern)

        for i in range(length):
            if pattern[i] not in pattern1:
                pattern1[pattern[i]] = s[i]
            else:
                if pattern1[pattern[i]] != s[i]:
                    return False
            if s[i] not in pattern2:
                pattern2[s[i]] = pattern[i]
            else:
                if pattern2[s[i]] != pattern[i]:
                    return False
        else:
            return True

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        iso1 = dict()
        iso2 = dict()
        length = len(s)

        for i in range(length):
            if s[i] not in iso1:
                iso1[s[i]] = t[i]
            else:
                if t[i] != iso1[s[i]]:
                    return False

        for i in range(length):
            if t[i] not in iso2:
                iso2[t[i]] = s[i]
            else:
                if s[i] != iso2[t[i]]:
                    return False
        
        return True
        

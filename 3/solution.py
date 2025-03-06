class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0

        start = 0
        end = 0
        longest = 0

        chars = set()
        chars.add(s[0])

        while end < len(s):
            if end == len(s)-1: break
            if s[end+1] in chars:
                while True:
                    if s[start] == s[end+1]:
                        start+=1
                        break
                    else:
                        chars.remove(s[start])
                        start+=1
                end += 1
            else:
                chars.add(s[end+1])
                end += 1
            longest = max(longest, end-start+1)
        longest = max(longest, end-start+1)
        return longest

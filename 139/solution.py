class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        size = len(s)+1
        n = len(wordDict)
        minimum = len(min(wordDict, key = len))
        maximum = len(max(wordDict, key = len))+1
        dp = [False] * size
        dp[0] = True
        
        for j in range(minimum, size):
            for i in range(minimum, maximum):
                dp[j] = dp[j] or (dp[j-i] and s[j-i:j] in wordDict)
        
        
        return dp[size-1]

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        size = len(s)+1
        minimum = len(min(wordDict, key = len))
        maximum = len(max(wordDict, key = len))+1
        dp = [False] * size
        dp[0] = True
        
        for i in range(minimum, size):
            for j in range(minimum, maximum):
                dp[i] = dp[i] or (dp[i-j] and s[i-j:i] in wordDict)
        
        
        return dp[size-1]

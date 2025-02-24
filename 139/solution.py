class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordLen = set()
        for i in wordDict:
            wordLen.add(len(i))
        dp = [True] + [False]*len(s)
        wordDict = set(wordDict)
        wordLen = list(wordLen)

        for i in range(1, len(s)+1):
            for j in wordLen:
                start = i-j
                if start >= 0 and dp[start] and s[start:i] in wordDict:
                    dp[i] = True

        return dp[-1]

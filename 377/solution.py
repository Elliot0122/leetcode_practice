class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = []
        for i in range(target+1):
            dp.append(0)
        dp[0] = 1
        for i in range(target):
            for j in nums:
                if i + j <= target:
                    dp[i+j]+=dp[i]
        return dp[target]

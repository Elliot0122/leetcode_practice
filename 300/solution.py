class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [nums[0]]
        for i in nums:
            if i < dp[0]:
                dp[0] = i
            elif i > dp[-1]:
                dp.append(i)
            else:
                dp[self.binary_search(dp, i)] = i
        return len(dp)
            
    def binary_search(self, nums, target):
        if len(nums) == 0:
            return 0
        start = 0
        end = len(nums)-1
        while start < end:
            mid = (start+end)/2
            if nums[mid] < target:
                start = mid+1
            else:
                end = mid
        return end

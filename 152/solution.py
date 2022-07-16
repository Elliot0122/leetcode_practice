class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = nums[0]
        tmax = 1
        tmin = 1
        for i in range(len(nums)):
            temp = tmax*nums[i]
            tmax = max(tmax*nums[i], tmin*nums[i], nums[i])
            tmin = min(temp, tmin*nums[i], nums[i])
            ans = max(ans, tmax, tmin)
        return ans

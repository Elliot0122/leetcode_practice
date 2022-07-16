class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        temp = 1
        ans = [ 1 for i in nums]
        for index, value in enumerate(nums):
            ans[index] *= temp
            temp *= value
        temp = 1
        for index in range(length-1, -1, -1):
            ans[index] *= temp
            temp *= nums[index]
        return ans

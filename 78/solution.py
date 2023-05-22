class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums, cur):
            if len(nums) == 0:
                return [cur]
            ans = []
            ans += dfs(nums[1:], cur)
            ans += dfs(nums[1:], cur+[nums[0]])
            return ans
        return dfs(nums, [])

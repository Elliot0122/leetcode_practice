class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numdict = {}
        for i in range(len(nums)):
            if target-nums[i] in numdict:
                return [numdict[target-nums[i]], i]
            else:
                numdict[nums[i]] = i

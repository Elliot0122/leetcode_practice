class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while right > left+1:
            if nums[right] < nums[(left+right)/2]:
                left = (left+right)/2
            else:
                right = (left+right)/2
        return min(nums[right], nums[left])
        

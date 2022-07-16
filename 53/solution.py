class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = nums[0]
        tempsum = nums[0]
        for i in range(1, len(nums)):
            tempsum += nums[i]
            tempsum = max(tempsum, nums[i])
            sum = max(sum, tempsum)
        return sum
                
            
        
        

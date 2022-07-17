class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)-1
        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        
        while end > start+1:
            mid = (start + end)/2
            if nums[mid] == target:
                return mid
            
            if nums[mid] < nums[end]:
                if nums[mid] <= target and target <= nums[end]:
                    start = mid
                else:
                    end = mid
            else:
                if nums[start] <= target and target <= nums[mid]:
                    end = mid
                else:
                    start = mid

        return -1
        

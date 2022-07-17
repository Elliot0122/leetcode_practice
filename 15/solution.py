class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        
        nums.sort()
        ans = set()
        for i in range(len(nums)-2):
            target = -nums[i]
            if target < 0:
                break
            dic = {}
            for j in range(i+1, len(nums)):
                if target-nums[j] in dic:
                    ans.add((nums[i], target-nums[j], nums[j]))
                else:
                    dic[nums[j]] = j
        return ans
        
        

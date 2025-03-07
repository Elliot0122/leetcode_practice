class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        occur = defaultdict()
        for i in range(len(nums)):
            if nums[i] not in occur:
                occur[target-nums[i]] = i
            else:
                return [occur[nums[i]], i]

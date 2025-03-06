class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target: return 0

        start = 0
        end = -1
        ttl = 0
        length = len(nums)

        while end < len(nums):
            if ttl < target:
                end += 1
                if end == len(nums):
                    break
                ttl += nums[end]
            else:
                length = min(length, end-start+1)
                ttl -= nums[start]
                start += 1

        length = min(length, end-start+1)
        return length

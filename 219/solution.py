class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        occur = set()

        for i in range(len(nums)):
            if i > k:
                occur.remove(nums[i-k-1])
            if nums[i] not in occur:
                occur.add(nums[i])
            else:
                return True
        
        return False

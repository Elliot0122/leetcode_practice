class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return []

        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i+1
            k = len(nums)-1
            while j<k:
                temp = nums[i]+nums[j]+nums[k]
                if temp > 0:
                    k -= 1
                elif temp < 0:
                    j += 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1

        return ans

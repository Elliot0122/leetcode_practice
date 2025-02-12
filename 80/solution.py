class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        cnt = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[k-1]:
                if cnt == 1:
                    nums[k] = nums[i]
                    cnt += 1
                    k += 1
            else:
                nums[k] = nums[i]
                cnt = 1
                k += 1
        return k

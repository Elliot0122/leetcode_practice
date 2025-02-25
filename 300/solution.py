class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []

        def binary_search(res, n):
            left = 0
            right = len(res)-1
            while left <= right:
                mid = (left+right)//2
                if res[mid] == n:
                    return mid
                elif res[mid] > n:
                    right = mid-1
                else:
                    left = mid+1

            return left

        for i in range(len(nums)):
            if not res or nums[i]>res[-1]:
                res.append(nums[i])
            else:
                temp = binary_search(res, nums[i])
                res[temp] = nums[i]

        return len(res)

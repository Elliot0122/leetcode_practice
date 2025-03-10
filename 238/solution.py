class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]*len(nums)
        temp = 1
        for i in range(len(nums)):
            output[i]*=temp
            temp*=nums[i]
        temp = 1
        for i in range(len(nums)-1, -1, -1):
            output[i]*=temp
            temp*=nums[i]

        return output

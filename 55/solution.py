class Solution:
    def canJump(self, nums: List[int]) -> bool:
        bools = [False]*len(nums)
        bools[0] = True
        
        for i in range(len(nums)):
            if bools[i]:
                bools[i+1:i+nums[i]+1] = [True]*nums[i]

        return bools[-1]

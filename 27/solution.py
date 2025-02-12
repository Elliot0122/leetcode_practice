class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        occurance = 0
        length = len(nums)

        for i in range(length):
            if nums[i] == val:
                occurance += 1
            else:
                nums[i-occurance] = nums[i]
        
        return length-occurance

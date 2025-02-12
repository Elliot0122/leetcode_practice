class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occurance = 0
        num = None

        for i in nums:
            if i != num:
                if occurance == 0:
                    num = i
                    occurance = 0
                else:
                    occurance -= 1
            else:
                occurance += 1

        return num
            

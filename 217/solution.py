class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numcnt = {}
        for i in nums:
            if i in numcnt:
                return True
            else:
                numcnt[i] = i
        return False

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 1
        pre = 1
        cur = 2
        for i in range(n-2):
            pre, cur = cur, pre+cur
        return cur

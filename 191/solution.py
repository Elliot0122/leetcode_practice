class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        mask = 1
        sum = 0
        for i in range(32):
            sum += n&mask
            n>>=1
        return sum
            

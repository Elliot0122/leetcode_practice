class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        sum = 0
        cnt = 0
        for i in range(32):
            sum += (n%2)
            n >>= 1
            sum <<= 1
        sum >>= 1
        return sum
        

class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        mask = 1
        listOfOnes = []
        for i in range(n+1):
            sum = 0
            for j in range(32):
                sum+=mask&i
                i>>=1
            listOfOnes.append(sum)
        return listOfOnes

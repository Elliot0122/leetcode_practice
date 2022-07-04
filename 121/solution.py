class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if len(prices) == 1:
            return 0
        minPrice = prices[0]
        profit = 0
        
        for i in prices:
            minPrice = min(minPrice, i)
            profit = max(profit, i-minPrice)
        return profit
        
            
            

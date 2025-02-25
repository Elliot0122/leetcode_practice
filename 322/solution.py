class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_amount = [0]+[amount+1]*amount

        for i in range(1, amount+1):
            for j in coins:
                if i-j >= 0:
                    min_amount[i] = min(min_amount[i], min_amount[i-j]+1)

        if min_amount[-1] == amount+1:
            return -1
        else:
            return min_amount[-1]

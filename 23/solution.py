class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def rec(cur, left, right):
            if left == 0 and right == 0:
                return [cur]
            ans = []
            if left > 0:
                ans += rec(cur+'(', left-1, right)
            if left < right:
                ans += rec(cur+')', left, right-1)
            return ans
        return rec('', n, n)

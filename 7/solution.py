class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        neg = False
        if x < 0:
            neg = True
            x = abs(x)
        while x:
            ans += x%10
            x = int(x/10)
            ans*=10
        ans= int(ans/10)
        if ans < -pow(2, 31):
            return 0
        elif ans > pow(2, 31)-1:
            return 0
        if neg:
            return -ans
        else:
            return ans

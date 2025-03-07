class Solution:
    def isHappy(self, n: int) -> bool:
        def digit_square_sum(num):
            ttl = 0
            while num != 0:
                ttl += (num%10)**2
                num = num//10
            return ttl
        
        occur = set()
        while n != 1:
            if n in occur: return False
            else:
                occur.add(n)
                n = digit_square_sum(n)

        return True

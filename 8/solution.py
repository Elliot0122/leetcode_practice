class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        head = 0
        cnt = 0
        nums = [f'{i}' for i in range(10)]
        neg = False
        spaces = True
        signed = True
        beforenumber = True
        number = True
        length = len(s)
        while True:
            if cnt == length:
                break
            if spaces:
                if s[cnt] != " ":
                    spaces = False
                    continue
            elif signed:
                signed = False
                if s[cnt] in nums:
                    continue
                if s[cnt] == "-":
                    neg = True
                elif s[cnt] == "+":
                    neg = False
                else:
                    return 0
            elif beforenumber:
                if s[cnt] not in nums:
                    return 0
                else:
                    beforenumber = False
                    head = cnt
                    continue
            elif number:
                if s[cnt] not in nums:
                    break
            cnt+=1
        if spaces or signed or beforenumber:
            return 0
        if neg:
            ans = -int(s[head:cnt])
            if ans < -pow(2, 31):
                return -pow(2, 31)
        else:
            ans = int(s[head:cnt])
            if ans > pow(2, 31)-1:
                return pow(2, 31)-1
        return ans


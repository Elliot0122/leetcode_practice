class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ttl_length = len(s)
        ans_length = 1
        ans = s[0]
        for index in range(ttl_length):
            length = 0
            while index - length >=0 and index + length < ttl_length:
                if s[index-length] != s[index+length]: break
                length+=1 
            length-=1
            if ans_length < length*2+1:
                ans_length = length*2+1
                ans = s[index-length:index+length+1]
                
            length = 0
            if ttl_length > 1:
                while index - length >= 0 and index + length + 1 < ttl_length:
                    if s[index-length] != s[index+length+1]: break
                    length+=1
                if ans_length < length*2:
                    ans_length = length*2
                    ans = s[index-length+1:index+length+1]
        return ans

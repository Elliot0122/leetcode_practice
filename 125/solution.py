class Solution:
    def isPalindrome(self, s: str) -> bool:
        all_char = []
        for i in s:
            if i.isalnum():
                all_char.append(i.lower())

        start = 0
        end = len(all_char)-1
        while start < end:
            if all_char[start] != all_char[end]:
                return False
            else:
                start+=1
                end -= 1
        return True

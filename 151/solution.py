class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split(" ")[::-1]
        ans = ""
        for i in words:
            if i != "":
                ans+=i
                ans+=" "

        return ans.strip()

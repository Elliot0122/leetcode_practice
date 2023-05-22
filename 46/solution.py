class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in nums:
            if len(ans) == 0:
                ans.append([i])
                continue
            temp = ans
            ans = []
            for j in temp:
                for k in range(len(j)+1):
                    new_ = j.copy()
                    new_.insert(k, i)
                    ans.append(new_)

        return ans

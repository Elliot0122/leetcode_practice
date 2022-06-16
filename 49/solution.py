class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            st = ''.join(sorted(s))
            ans[st].append(s)
        return ans.values()

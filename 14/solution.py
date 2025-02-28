class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = []
        cur = None
        cnt = 0
        while True:
            if cnt < len(strs[0]):
                cur = strs[0][cnt]
            else:
                return ''.join(common_prefix)
            for i in range(1, len(strs)):
                if cnt == len(strs[i]) or strs[i][cnt] != cur:
                    return ''.join(common_prefix)
            else:
                cnt += 1
                common_prefix.append(cur)

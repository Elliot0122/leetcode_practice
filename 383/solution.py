class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_map = dict()
        ransom = set()
        mag_map = dict()
        mag = set()

        for i in ransomNote:
            if i not in ransom:
                ransom_map[i] = 1
                ransom.add(i)
            else:
                ransom_map[i] += 1

        for i in magazine:
            if i not in mag:
                mag_map[i] = 1
                mag.add(i)
            else:
                mag_map[i] += 1

        ransom = list(ransom)
        for i in ransom:
            if i not in mag:
                return False
            else:
                if ransom_map[i] > mag_map[i]:
                    return False
        else:
            return True

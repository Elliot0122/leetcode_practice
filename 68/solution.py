class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def construct_line(cur_word, cur_len, maxWidth, last):
            if last:
                res = ""
                for i in cur_word:
                    res += i
                    if i != cur_word[-1]:
                        res += " "
                res += " "*(maxWidth-len(res))
            else:
                if len(cur_word) == 1:
                    res = cur_word[0]
                    res += " "*(maxWidth-len(res))
                else:
                    spaces = (maxWidth-cur_len)//(len(cur_word)-1)
                    extra = maxWidth-cur_len-(spaces)*(len(cur_word)-1)
                    res = ""
                    for j in range(len(cur_word)):
                        res += cur_word[j]
                        if j != len(cur_word)-1:
                            res += " "*spaces
                            if extra:
                                res += " "
                                extra-=1

            return res

        output = []
        cur_word = [words[0]]
        cur_len = len(words[0])
        for i in range(1, len(words)):
            if cur_len + len(cur_word) + len(words[i]) > maxWidth:
                output.append(construct_line(cur_word, cur_len, maxWidth, False))
                cur_word = [words[i]]
                cur_len = len(words[i])
            else:
                cur_len += len(words[i])
                cur_word.append(words[i])
        output.append(construct_line(cur_word, cur_len, maxWidth, True))
        return output

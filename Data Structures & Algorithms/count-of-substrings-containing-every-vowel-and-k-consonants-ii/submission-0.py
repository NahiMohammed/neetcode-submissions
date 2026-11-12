class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)

        def atLeast(k):
            cnt = {}
            cons = 0
            l = 0
            res = 0
            for r, c in enumerate(word):
                if c in "aeiou":
                    cnt[c] = cnt.get(c, 0) + 1
                else:
                    cons += 1
                while len(cnt) == 5 and cons >= k:
                    res += n - r
                    d = word[l]
                    if d in "aeiou":
                        cnt[d] -= 1
                        if cnt[d] == 0:
                            del cnt[d]
                    else:
                        cons -= 1
                    l += 1
            return res

        return atLeast(k) - atLeast(k + 1)
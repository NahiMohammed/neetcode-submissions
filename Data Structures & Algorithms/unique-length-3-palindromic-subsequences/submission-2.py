class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        l = 0
        r = n - 1
        res= 0
        extreme = set()
        for l in range(0, n - 2):
            for r in range(n - 1, l + 1, -1):
                if s[r] == s[l] and s[r] not in extreme:
                    extreme.add(s[r])
                    middle = set()
                    for m in range(l + 1, r):
                        middle.add((s[m]))
                    res+=len(middle)

        return res

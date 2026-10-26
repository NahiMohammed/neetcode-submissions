class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = {}
        last = {}

        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i

        res = 0

        for c in first:
            l, r = first[c], last[c]

            if r - l >= 2:
                res += len(set(s[l + 1:r]))

        return res
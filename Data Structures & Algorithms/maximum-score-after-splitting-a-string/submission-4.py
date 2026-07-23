class Solution:
    def maxScore(self, s: str) -> int:
        curr = (s[0] == "0")

        for c in s[1:]:
            if c == "1":
                curr += 1

        res = curr

        for i in range(1, len(s) - 1):
            if s[i] == "0":
                curr += 1
            else:
                curr -= 1

            res = max(res, curr)

        return res
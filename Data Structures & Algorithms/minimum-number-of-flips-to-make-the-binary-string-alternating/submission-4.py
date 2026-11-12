class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        t = s + s
        diff1 = 0          # mismatches against 0101...
        res = n
        for i in range(len(t)):
            if int(t[i]) != i % 2:
                diff1 += 1
            if i >= n:
                if int(t[i - n]) != (i - n) % 2:
                    diff1 -= 1
            if i >= n - 1:
                res = min(res, diff1, n - diff1)
        return res
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = 0
        res = 0
        count = defaultdict(int)
        n = len(s)

        for r in range(n):
            count[s[r]] += 1

            while len(count) == 3:
                res += n - r
                count[s[l]] -= 1

                if count[s[l]] == 0:
                    del count[s[l]]

                l += 1

        return res
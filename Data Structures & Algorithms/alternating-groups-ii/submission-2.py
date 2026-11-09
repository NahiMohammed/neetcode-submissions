class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        res = 0
        count = 1

        for i in range(1, n + k - 1):
            if colors[i % n] != colors[(i - 1) % n]:
                count += 1
            else:
                count = 1

            if count >= k:
                res += 1

        return res
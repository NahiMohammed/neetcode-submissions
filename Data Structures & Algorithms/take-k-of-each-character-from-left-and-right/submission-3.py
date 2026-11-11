class Solution:
    def takeCharacters(self, s: str, k: int) -> int:

        n = len(s)
        total = [0, 0, 0]
        for c in s:
            total[ord(c) - 97] += 1
        if min(total) < k:
            return -1

        limit = [t - k for t in total]

        cnt = [0, 0, 0]
        left = 0
        best = 0

        for right, c in enumerate(s):
            i = ord(c) - ord("a")
            cnt[i] += 1
            while cnt[i] > limit[i]:
                cnt[ord(s[left]) - ord("a")] -= 1
                left += 1
            best = max(best, right - left + 1)

        return n - best

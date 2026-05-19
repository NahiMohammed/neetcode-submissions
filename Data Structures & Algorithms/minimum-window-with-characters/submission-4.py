from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)
        window = defaultdict(int)

        have = 0
        need_count = len(need)

        res = (float("inf"), 0, 0)  # length, left, right

        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] += 1

            if c in need and window[c] == need[c]:
                have += 1

            while have == need_count:
                # update answer
                if (r - l + 1) < res[0]:
                    res = (r - l + 1, l, r)

                # shrink from left
                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1

                l += 1

        return "" if res[0] == float("inf") else s[res[1]:res[2]+1]
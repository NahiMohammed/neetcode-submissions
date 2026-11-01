class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        n = len(s)
        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] in window:
                while s[r] in window:
                    window.discard(s[l])
                    l += 1

            else:
                res = max(res, r - l + 1)
            window.add(s[r])
        return res

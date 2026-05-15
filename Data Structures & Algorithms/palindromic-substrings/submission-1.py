class Solution:
    def extend(self, s: str, left: int, right: int):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            self.res += 1
            left -= 1
            right += 1

    def countSubstrings(self, s: str) -> int:
        self.res = 0
        for i in range(len(s)):
            self.extend(s, i, i)
            self.extend(s, i, i + 1)
        return self.res

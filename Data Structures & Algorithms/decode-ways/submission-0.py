class Solution:
    def decode(self, s, i):
        if i == len(s):
            return 1
        if s[i] == "0":
            return 0

        res = self.decode(s, i + 1)

        if i + 1 < len(s) and int(s[i:i+2]) <= 26:
            res += self.decode(s, i + 2)

        return res

    def numDecodings(self, s: str) -> int:
        return self.decode(s, 0)
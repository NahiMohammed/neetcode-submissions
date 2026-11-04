class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def dp(i):
            if i == len(s):
                return 1

            if s[i] == '0':
                return 0

            if i in memo:
                return memo[i]

            # Decode one digit
            res = dp(i + 1)

            # Decode two digits if valid
            if i + 1 < len(s) and int(s[i:i+2]) <= 26:
                res += dp(i + 2)

            memo[i] = res
            return res

        return dp(0)
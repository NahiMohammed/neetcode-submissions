class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        last_index = 0
        for i in range(len(s)):
            found = False
            for j in range(last_index, len(t)):
                if s[i] == t[j]:
                    found = True
                    last_index = j + 1
                    break
            if not found:
                return False
        return True

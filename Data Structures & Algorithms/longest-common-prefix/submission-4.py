
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        for j in range(len(strs[0])):
            for k in range(1, len(strs)):
                if j >= len(strs[k]) or strs[k][j] != strs[0][j]:
                    return strs[0][:j]

        return strs[0]